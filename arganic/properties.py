from typing import Type, Any, final, Callable
from arganic.validators import Validator


class Property:

    def __init__(self, **kwargs: str | Type | bool | tuple | int | dict) -> None:
        self.__default: Any = kwargs.get('default', None)
        self.name: str = ''
        self.__read_only: bool = kwargs.get('read_only', True)
        self.__required: bool = kwargs.get('required', True)
        self.__type: Type = kwargs.get('type', Any)
        self.__validators: tuple[Validator] = kwargs.get('validators', ())
        self.__choices: tuple = kwargs.get('choices')
        if self.default is not None:
            self.validate(self.default)
        if self.choices:
            for choice in self.choices:
                self.validate(choice)

    def validate(self, value) -> bool:
        # Test type
        if (
                value is not None
                and self.type is not Any
                and not isinstance(value, self.type)
        ):
            raise TypeError(f'Option {self.name}: the Value "{value}" is not of type "{self.__type}".')
        # Test for required
        if (
                self.required
                and not value
                and value is not False
                and self.default is None
        ):
            raise ValueError(f'Option {self.name}: is required.')
        # Check choices
        if (
                self.choices
                and (self.required or value is not None)
                and value not in self.choices
        ):
            raise ValueError(f'Option {self.name}: needs to be one of {self.__choices}.')
        # process all validators
        # map(lambda obj: getattr(obj, 'validate')(value), self.validators)
        if value is not None:
            for validator in self.validators:
                validator.validate(value)
        return True

    @property
    def choices(self) -> tuple:
        return self.__choices

    @property
    def default(self) -> Any:
        return self.__default

    @property
    def read_only(self) -> bool:
        return self.__read_only

    @property
    def required(self) -> bool:
        return self.__required

    @property
    def type(self) -> Type:
        return self.__type

    @property
    def validators(self) -> tuple[Validator]:
        return self.__validators


class Properties:

    __properties: dict[str, dict[str, Property]] = {}

    @staticmethod
    def set_properties(decorated: type, props: dict[str, Property]):
        if not Properties.has_properties(decorated):
            for key, value in props.items():
                value.name = key
            decorated_id = Properties.get_decorated_id(decorated)
            Properties.__properties[decorated_id] = props

    @staticmethod
    def has_properties(decorated: type) -> bool:
        decorated_id = Properties.get_decorated_id(decorated)
        return Properties.__properties.get(decorated_id) is not None

    @staticmethod
    def get_decorated_id(decorated: type | Callable) -> str:
        return '.'.join(
            [decorated.__module__, decorated.__qualname__]
        )

    def __init__(self, *args, **kwargs) -> None:
        self.__values: dict = args[0] if args else kwargs
        self.__decorated:str = ''

    def set_decorated(self, decorated):
        self.__decorated = Properties.get_decorated_id(
            decorated
        )

    def get_property(self, name: str) -> Property:
        prop = Properties.__properties.get(
            self.__decorated).get(name)
        if prop:
            return prop

        raise KeyError(f'The property {name} not exists for {self.__decorated}.')

    @final
    def get(self, key: str) -> Any:
        return self.__values.get(
            key,
            self.get_property(key).default
        )

    @final
    def set(self, key: str, value: Any) -> None:
        if self.get_property(key).read_only:
            raise ValueError(f'The property {key} is read-only in {self.__decorated}.')
        if self.get_property(key).validate(value):
            self.__values[key] = value

    @final
    def validate(self) -> bool:
        props = Properties.__properties.get(self.__decorated)
        for key, prop in props.items():
            prop.validate(self.__values.get(key))
        return True


def class_properties(**_properties):
    def properties_decorator(decorated_class) -> Type:
        class ClassProperties(decorated_class):
            def __init__(self, *args, **kwargs) -> None:
                Properties.set_properties(decorated_class, _properties)
                super().__init__(*args, **kwargs)
                super().set_decorated(decorated_class)
                super().validate()
        return ClassProperties
    return properties_decorator


# Method arguments decorator
def method_arguments(**_arguments):
    def arguments_decorator(decorated_func) -> Callable:
        def method(instance, *args, **kwargs):
            Properties.set_properties(decorated_func, _arguments)
            props = Properties(*args, **kwargs)
            props.set_decorated(decorated_func)
            props.validate()
            return decorated_func(instance, *args, **kwargs)
        return method
    return arguments_decorator
