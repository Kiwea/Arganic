from arganic.arguments import function_arguments, Argument
from arganic.validators import File


@function_arguments(
    file=Argument(
        type=str,
        validator=File()
    )
)
def file_handler(*args, **kwargs) -> str:
    print(file_handler.arguments.get('file'))
    return file_handler.arguments.get('file')


# Validation
file_handler(file='tests/examples/validate_dir/validate_file.txt')
