from arganic.arguments import function_arguments, Argument
from arganic.validators import Validator


class CityValidator(Validator):
    """
    Custom validator class.
    """
    def validate(self, value) -> bool:
        if value in ('Geneva', 'Paris', 'Lyon', 'Madrid'):
            return True
        raise ValueError('Invalid value')


@function_arguments(
    start=Argument(
        type=str,
        validator=CityValidator()
    ),
    destination=Argument(
        type=str,
        validator=CityValidator()
    )
)
def drive(*args, **kwargs) -> None:
    print('Drive')
    print('start', drive.arguments.get('start'))
    print('destination', drive.arguments.get('destination'))
    return drive.arguments.values


drive(start='Geneva', destination='Paris')
drive(start='Lyon', destination='Geneva')
drive(start='Madrid', destination='Paris')
