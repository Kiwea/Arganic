import os.path
import errno
import re
from abc import abstractmethod, ABC


class Validator(ABC):
    """
    Abstract class for validators
    """

    def __init__(self):
        pass

    @abstractmethod
    def validate(self, value) -> bool:
        """
        Abstract method to validate
        Parameters
        ----------
        value

        Returns
        -------

        """
        pass


class MinLength(Validator):
    """
    Minimum length
    """

    def __init__(self, min_length: int) -> None:
        self.__min_length = min_length
        super().__init__()

    def validate(self, value) -> bool:
        """
        Validate Minl ength
        Parameters
        ----------
        value

        Returns
        -------

        """
        if len(value) < self.__min_length:
            raise ValueError(f"Min length is {self.__min_length}")
        return True


class Url(Validator):
    """
    URL Validator
    """
    def validate(self, value) -> bool:
        """
        Validate URL
        Parameters
        ----------
        value

        Returns
        -------

        """
        pattern = r'^(?:http|ftp)s?://'
        if not re.match(pattern, value):
            raise ValueError(f"Url not valid {value}")
        return True


class Email(Validator):
    """
    Email Validator
    """
    def validate(self, value) -> bool:
        """
        Validate Email
        Parameters
        ----------
        value

        Returns
        -------

        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError(f"Email not valid {value}")
        return True


class MaxLength(Validator):
    """
    Max length validator
    """

    def __init__(self, max_length: int) -> None:
        self.__max_length = max_length
        super().__init__()

    def validate(self, value) -> bool:
        """
        Validate Max length

        Parameters
        ----------
        value

        Returns
        -------

        """
        if len(value) > self.__max_length:
            raise ValueError(f"Max length is {self.__max_length}")
        return True


class File(Validator):
    """
    File Validator
    """
    def validate(self, value) -> bool:
        """
        Validate File
        Parameters
        ----------
        value

        Returns
        -------

        """
        if not os.path.isfile(value):
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                value
            )
        return True


class Dir(Validator):
    """
    Dir Validator
    """
    def validate(self, value) -> bool:
        """
        Validate Dir
        Parameters
        ----------
        value

        Returns
        -------

        """
        if not os.path.isdir(value):
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                value
            )
        return True
