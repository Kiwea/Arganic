import os.path
import errno
import re
from abc import abstractmethod, ABC


class Validator(ABC):
    """
    Base class for validators.

    It's possible to define your own validators by extending this class.

    Examples
    --------

    Example of a custom validator.

    ``` py linenums="1" hl_lines="5-12 15-24"
    --8<-- "tests/examples/custom_validator.py"
    ```
    """

    def __init__(self):
        pass

    @abstractmethod
    def validate(self, value) -> bool:
        """
        Override this method on inherited classes.

        Parameters
        ----------
        value
            The value to validate.

        Returns
        -------
        bool
            The validate() methods needs to return True if the
            validation pass or raises an exception if the validation fails.
        """
        pass


class Dir(Validator):
    """
    Directory Validator.
    """
    def validate(self, value) -> bool:
        """
        Test the existence of a directory according to the path provided.

        Parameters
        ----------
        value: str
            Path to the directory that must exist on the file system.
        Returns
        -------
        bool
            True if the directory exists.
        Raises
        ------
        FileNotFoundError
            If the directory does not exist on the file system.

        Examples
        --------

        ``` py linenums="1" hl_lines="8 17"
        --8<-- "tests/examples/validator_dir.py"
        ```

        <hr />
        """
        if not os.path.isdir(value):
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                value
            )
        return True


class Email(Validator):
    """
    Email address Validator.
    """
    def validate(self, value) -> bool:
        """
        Validates the syntax of an email address.
        Parameters
        ----------
        value: str
            Email address whose syntax must be checked.

        Returns
        -------
        bool
            If the value provided is a correct email address format.

        Raises
        ------
        ValueError
            If the value provided is not a valid email address.
        Examples
        --------

        ``` py linenums="1" hl_lines="8 17"
        --8<-- "tests/examples/validator_email.py"
        ```

        <hr />
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError(f"The value provided: '{value}' is not a "
                             f"correctly formatted email address.")
        return True


class File(Validator):
    """
    File Validator
    """
    def validate(self, value) -> bool:
        """
        Test the existence of a file according to the path provided.

        Parameters
        ----------
        value: str
            Path to the file that must exist on the file system.
        Returns
        -------
        bool
            True if the file exists.
        Raises
        ------
        FileNotFoundError
            If the file does not exist on the file system.

        Examples
        --------

        ``` py linenums="1" hl_lines="8 17"
        --8<-- "tests/examples/validator_file.py"
        ```

        <hr />
        """
        if not os.path.isfile(value):
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                value
            )
        return True


class MaxLength(Validator):
    """
    Maximum length validator.
    """

    def __init__(self, max_length: int) -> None:
        """
        Max length Validator constructor.

        Parameters
        ----------
        max_length: int
            The maximum length that the values to validate must not exceed.
        """
        self.__max_length = max_length
        super().__init__()

    def validate(self, value) -> bool:
        """
        Validates a value whose maximum length must not be
        greater than the value specified in the validator constructor.

        The value must be of a type supporting the builtin
        [len()](https://docs.python.org/3/library/functions.html#len)
        Python function.

        Parameters
        ----------
        value
            The value to validate.

        Returns
        -------
        bool
            True if the validation succeeded.

        Raises
        ------
        TypeError
            If the length of the value is longer than the
            specified maximum length.

        Examples
        --------

        ``` py linenums="1" hl_lines="8 19 28 30"
        --8<-- "tests/examples/validator_max_length.py"
        ```

        <hr />
        """
        if len(value) > self.__max_length:
            raise ValueError(f"The length of the value: '{value}' "
                             f"is longer than the specified"
                             f"maximum length: {self.__max_length}")
        return True


class MinLength(Validator):
    """
    Minimum length validator.
    """

    def __init__(self, min_length: int) -> None:
        """
        Max length Validator constructor.

        Parameters
        ----------
        min_length: int
            The minimum length that the value must be.
        """
        self.__min_length = min_length
        super().__init__()

    def validate(self, value) -> bool:
        """
        Verifies that the provided value have a length must be
        at least the minimum value given in the validator constructor.

        The value must be of a type supporting the builtin
        [len()](https://docs.python.org/3/library/functions.html#len)
        Python function.

        Parameters
        ----------
        value
            The value to validate.

        Returns
        -------
        bool
            True if the validation succeeded.

        Raises
        ------
        TypeError
            If the length of the value is shorter than the
            specified minimum length.

        Examples
        --------

        ``` py linenums="1" hl_lines="8 18 27 29"
        --8<-- "tests/examples/validator_min_length.py"
        ```

        <hr />
        """
        if len(value) < self.__min_length:
            raise ValueError(f"The length of the value: '{value}' "
                             f"is shorter than the specified"
                             f"minimum length: {self.__min_length}")
        return True


class Url(Validator):
    """
    URL Validator.
    """
    def validate(self, value) -> bool:
        """
        Validate if an URL is well formatted.
        supported protocols: http, https, ftp, ftps.

        Parameters
        ----------
        value: str
            The value of the URL to validate.

        Returns
        -------
        bool
            True if the URL is well formatted.

        Raises
        ------
        ValueError
            If the provided value is an invalid Url.

        Examples
        --------

        ``` py linenums="1" hl_lines="8 17"
        --8<-- "tests/examples/validator_url.py"
        ```

        <hr />
        """
        pattern = r'^(?:http|ftp)s?://'
        if not re.match(pattern, value):
            raise ValueError(f"The Url: {value} is not well formatted.")
        return True
