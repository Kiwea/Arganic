import os.path
import errno
import re
from abc import abstractmethod, ABC


class Validator(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def validate(self, value) -> bool:
        pass


class MinLength(Validator):

    def __init__(self, min_length: int) -> None:
        self.__min_length = min_length
        super().__init__()

    def validate(self, value) -> bool:
        if len(value) < self.__min_length:
            raise ValueError(f"Min length is {self.__min_length}")
        return True


class Url(Validator):
    def validate(self, value) -> bool:
        pattern = r'^(?:http|ftp)s?://'
        if not re.match(pattern, value):
            raise ValueError(f"Url not valid {value}")
        return True


class Email(Validator):
    def validate(self, value) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError(f"Email not valid {value}")
        return True


class MaxLength(Validator):

    def __init__(self, max_length: int) -> None:
        self.__max_length = max_length
        super().__init__()

    def validate(self, value) -> bool:
        if len(value) > self.__max_length:
            raise ValueError(f"Max length is {self.__max_length}")
        return True


class File(Validator):
    def validate(self, value) -> bool:
        if not os.path.isfile(value):
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                value
            )
        return True


class Dir(Validator):
    def validate(self, value) -> bool:
        if not os.path.isdir(value):
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                value
            )
        return True
