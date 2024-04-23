from arganic.validators import MinLength
from arganic.arguments import function_arguments, Argument


@function_arguments(
    min_len=Argument(
        type=str,
        validator=MinLength(1)
    )
)
def min_len_1_handler(*args, **kwargs) -> str:
    return min_len_1_handler.arguments.get('min_len')


@function_arguments(
    min_len=Argument(
        type=str,
        validator=MinLength(10)
    )
)
def min_len_10_handler(*args, **kwargs) -> str:
    print(min_len_10_handler.arguments.get('min_len'))
    return min_len_10_handler.arguments.get('min_len')


# Validation
min_len_1_handler(min_len='example')
# Validation
min_len_1_handler(min_len='example1234')