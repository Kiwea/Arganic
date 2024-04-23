from arganic.arguments import function_arguments, Argument
from arganic.validators import Dir


@function_arguments(
    dir=Argument(
        type=str,
        validator=Dir()
    )
)
def dir_handler(*args, **kwargs) -> str:
    print(dir_handler.arguments.get('dir'))
    return dir_handler.arguments.get('dir')


# Validation
dir_handler(dir='tests/examples/validate_dir')
