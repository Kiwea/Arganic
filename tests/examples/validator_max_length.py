from arganic.validators import MaxLength
from arganic.arguments import function_arguments, Argument


@function_arguments(
    max_len=Argument(
        type=str,
        validator=MaxLength(10)
    )
)
def max_len_10_handler(*args, **kwargs) -> str:
    print(max_len_10_handler.arguments.get('max_len'))
    return max_len_10_handler.arguments.get('max_len')


@function_arguments(
    max_len=Argument(
        type=str,
        validator=MaxLength(1)
    )
)
def max_len_1_handler(*args, **kwargs) -> str:
    print(max_len_1_handler.arguments.get('max_len'))
    return max_len_1_handler.arguments.get('max_len')


# Validation
max_len_10_handler(max_len='example')
# Validation
max_len_1_handler(max_len='e')
