from typing import Type, Any, Callable
from arganic.validators import Validator


class Argument:
    """Represents an argument with various properties.

    This class represents an argument with the following properties:

    Attributes
    ----------
    name : str
        The name of the argument.
    default : Any, optional
        The default value of the argument.
    read_only : bool, default=True
        Whether the argument is read-only.
    required : bool, default=True
        Whether the argument is required.
    type : Type | tuple[Type], optional
        The data type of the argument value.
    validator : Validator | tuple[Validator], optional
        A Validator object or list of Validator objects used to validate the argument value.
    choices : tuple, optional
        A tuple of choices the argument value can take.

    Methods
    -------
    validate(value)
        Validate the argument value based on the specified rules.

    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the Argument object with specified properties.

        Parameters
        ----------
        *args : Any
            Variable length argument list.
        **kwargs : Any
            Arbitrary keyword arguments.
       """
        kwargs = args[0] if args else kwargs
        self.__default: Any = kwargs.get('default', None)
        self._name: str = ''
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

    @property
    def name(self) -> str:
        """
        Get the name of the argument
        Returns
        -------
        str
        """
        return self._name

    @property
    def choices(self) -> tuple:
        """
        Get the values choices of the argument.

        Returns
        -------
        tuple
            A tuple of choices the argument value can take.
        """
        return self.__choices

    @property
    def default(self) -> Any:
        """
        Get the default value of the argument.

        Returns
        -------
        Any
            The default value of the argument.
        """
        return self.__default

    @property
    def read_only(self) -> bool:
        """
        Check if the argument is read-only.

        Returns
        -------
        bool
            True if the argument is read-only, False otherwise.
        """
        return self.__read_only

    @property
    def required(self) -> bool:
        """
        Check if the argument is required.

        Returns
        -------
        bool
            True if the argument is required, False otherwise.
        """
        return self.__required

    @property
    def type(self) -> Type | tuple[Type]:
        """
        Get the data type(s) the argument value can take.

        Returns
        -------
        Type | tuple[Type]
            The data type of the argument value.
        """
        return self.__type

    @property
    def validator(self) -> Validator | tuple[Validator]:
        """
        Get the validator(s) of the argument.

        Returns
        -------
        Validator | tuple[Validator]
            The validator function or a tuple of validator functions.
        """
        return self.__validator

    def validate(self, value: Any) -> bool:
        """
        Validate the argument value based on the specified rules.

        Parameters
        ----------
        value : Any
            The value to validate.

        Returns
        -------
        bool
            True if the value is valid, False otherwise.

        Raises
        ------
        TypeError
            If the value is not of the specified type.
        ValueError
            If the value is required but not provided, or if it is not among the specified choices.
        """
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
            raise ValueError(f'Option {self.name}: {value} needs to be one of {self.__choices}.')
        # process all validators
        # map(lambda obj: getattr(obj, 'validate')(value), self.validators)
        if value is not None:
            if isinstance(self.validator, Validator):
                self.validator.validate(value)
            elif isinstance(self.validator, tuple):
                for validator in self.validator:
                    validator.validate(value)
        return True


class ArgumentHandler:
    """
    Handles the management of arguments for decorated classes or functions.

    Methods
    -------
    get(key)
        Retrieves the value of a specified argument.

    set(key, value)
        Sets the value of a specified argument.
    """
    __arguments: dict[str, dict[str, Argument]] = {}

    @staticmethod
    def set_arguments(decorated: type, arguments: dict[str, Argument]):
        if not ArgumentHandler.__has_arguments(decorated):
            for key, value in arguments.items():
                value._name = key
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
        """
        Retrieves the value of a specified argument.

        Parameters
        ----------
        key : str
            The key of the argument.

        Returns
        -------
        Any
            The value of the specified argument.
        """
        return self.__values.get(
            key,
            self.__get_argument(key).default
        )

    def set(self, key: str, value: Any) -> None:
        """
        Sets the value of a specified argument.

        Parameters
        ----------
        key : str
            The key of the argument.
        value : Any
            The new value for the argument.

        Raises
        -------
        ValueError if the argument is allowed for read only.
        """
        if self.__get_argument(key).read_only:
            raise ValueError(f'The argument {key} is read-only in {self.__decorated}.')
        if self.__get_argument(key).validate(value):
            self.__values[key] = value

    def __validate(self) -> bool:
        props = ArgumentHandler.__arguments.get(self.__decorated)
        for key, prop in props.items():
            prop.validate(self.get(key))
        return True


def class_properties(**_properties):
    """
    Decorator for classes
    Parameters
    ----------
    _properties

    Returns
    -------

    """
    def properties_decorator(decorated_class) -> Type:
        class ClassProperties(decorated_class):
            def __init__(self, *args, **kwargs) -> None:
                ArgumentHandler.set_arguments(decorated_class, _properties)
                super().__init__(decorated_class, *args, **kwargs)
        return ClassProperties
    return properties_decorator


# Method arguments decorator
def method_arguments(**_arguments):
    """
    Decorator for class methods
    Parameters
    ----------
    _arguments

    Returns
    -------

    """
    def arguments_decorator(decorated_func) -> Callable:
        def method(instance, *args, **kwargs):
            ArgumentHandler.set_arguments(decorated_func, _arguments)
            method.arguments = ArgumentHandler(decorated_func, *args, **kwargs)
            return decorated_func(instance, *args, **kwargs)
        return method
    return arguments_decorator


def function_arguments(**_arguments):
    """
    Decorator for functions
    Parameters
    ----------
    _arguments

    Returns
    -------

    """
    def arguments_decorator(decorated_func) -> Callable:
        def function(*args, **kwargs):
            ArgumentHandler.set_arguments(decorated_func, _arguments)
            function.arguments = ArgumentHandler(decorated_func, *args, **kwargs)
            return decorated_func(*args, **kwargs)
        return function
    return arguments_decorator
