from typing import Type, Any, Callable
from arganic.validators import Validator


class Argument:

    def __init__(self, **kwargs: Any) -> None:
        self.__default: Any = kwargs.get('default', None)
        self.name: str = ''
        self.__read_only: bool = kwargs.get('read_only', True)
        self.__required: bool = kwargs.get('required', True)
        self.__type: Type | tuple[Type] = kwargs.get('type', Any)
        self.__validator: Validator | tuple[Validator] = kwargs.get('validator')
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
            if isinstance(self.validator, Validator):
                self.validator.validate(value)
            elif isinstance(self.validator, tuple):
                for validator in self.validator:
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
    def type(self) -> Type | tuple[Type]:
        return self.__type

    @property
    def validator(self) -> Validator | tuple[Validator]:
        return self.__validator


class ArgumentHandler:

    __arguments: dict[str, dict[str, Argument]] = {}

    @staticmethod
    def set_arguments(decorated: type, arguments: dict[str, Argument]):
        if not ArgumentHandler.__has_arguments(decorated):
            for key, value in arguments.items():
                value.name = key
            decorated_id = ArgumentHandler.__get_decorated_id(decorated)
            ArgumentHandler.__arguments[decorated_id] = arguments

    @staticmethod
    def __has_arguments(decorated: type) -> bool:
        decorated_id = ArgumentHandler.__get_decorated_id(decorated)
        return ArgumentHandler.__arguments.get(decorated_id) is not None

    @staticmethod
    def __get_decorated_id(decorated: type | Callable) -> str:
        return '.'.join(
            [decorated.__module__, decorated.__qualname__]
        )

    def __init__(self, decorated: type | Callable, *args, **kwargs) -> None:
        self.__values: dict = args[0] if args else kwargs
        self.__decorated: str = ArgumentHandler.__get_decorated_id(decorated)
        self.__validate()

    def __get_argument(self, name: str) -> Argument:
        prop = ArgumentHandler.__arguments.get(
            self.__decorated).get(name)
        if prop:
            return prop

        raise KeyError(f'The property {name} not exists for {self.__decorated}.')

    def get(self, key: str) -> Any:
        return self.__values.get(
            key,
            self.__get_argument(key).default
        )

    def set(self, key: str, value: Any) -> None:
        if self.__get_argument(key).read_only:
            raise ValueError(f'The property {key} is read-only in {self.__decorated}.')
        if self.__get_argument(key).validate(value):
            self.__values[key] = value

    def __validate(self) -> bool:
        props = ArgumentHandler.__arguments.get(self.__decorated)
        for key, prop in props.items():
            prop.validate(self.__values.get(key))
        return True


def class_properties(**_properties):
    def properties_decorator(decorated_class) -> Type:
        class ClassProperties(decorated_class):
            def __init__(self, *args, **kwargs) -> None:
                ArgumentHandler.set_arguments(decorated_class, _properties)
                super().__init__(decorated_class, *args, **kwargs)
                #super().validate()
        return ClassProperties
    return properties_decorator


# Method arguments decorator
def method_arguments(**_arguments):
    def arguments_decorator(decorated_func) -> Callable:
        def method(instance, *args, **kwargs):
            ArgumentHandler.set_arguments(decorated_func, _arguments)
            method.arguments = ArgumentHandler(decorated_func, *args, **kwargs)
            return decorated_func(instance, *args, **kwargs)
        return method
    return arguments_decorator


def function_arguments(**_arguments):
    def arguments_decorator(decorated_func) -> Callable:
        def function(*args, **kwargs):
            ArgumentHandler.set_arguments(decorated_func, _arguments)
            function.arguments = ArgumentHandler(decorated_func, *args, **kwargs)
            return decorated_func(*args, **kwargs)
        return function
    return arguments_decorator
