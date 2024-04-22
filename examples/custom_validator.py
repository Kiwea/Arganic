from arganic.arguments import function_arguments, Argument
from arganic.validators import Validator


class MyValidator(Validator):

    def validate(self, value) -> bool:
        if value in ('Geneva', 'Paris', 'Lyon', 'Madrid'):
            return True
        raise ValueError('Invalid value')


@function_arguments(
    start=Argument(
        type=str,
        validator=MyValidator()
    ),
    destination=Argument(
        type=str,
        validator=MyValidator()
    )
)
def drive(*args, **kwargs) -> None:
    print('Drive')
    print('start', drive.arguments.get('start'))
    print('destination', drive.arguments.get('destination'))


drive(start='Geneva', destination='Paris')
drive(start='Lyon', destination='Geneva')
drive(start='Madrid', destination='Paris')