from arganic.arguments import (
    class_properties,
    method_arguments,
    function_arguments,
    ArgumentHandler,
    Argument
)
from arganic.validators import (
    File,
    Dir,
    Email,
    Url,
    MaxLength,
    MinLength
)


@class_properties(
    int_prop=Argument(
        type=int,
        default=1,
        read_only=False
    ),
    is_required=Argument(),
    is_choices=Argument(
        type=str,
        choices=('a', 'b', 'c'),
        required=False
    ),
    is_dir=Argument(
        type=str,
        required=False,
        validator=Dir()
    ),
    is_file=Argument(
        type=str,
        required=False,
        validator=File()
    )
)
class DecoratedClass(ArgumentHandler):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print(self.get('int_prop'))

    def get_int_prop(self) -> int:
        return self.get('int_prop')

    @method_arguments(
        first_arg=Argument(
            type=float
        ),
        second_arg=Argument(
            type=str,
            validator=(MinLength(2), MaxLength(4)),
            required=False
        ),
        email=Argument(
            type=str,
            validator=Email(),
            required=False
        ),
        url=Argument(
            type=str,
            validator=Url(),
            required=False
        )
    )
    def decorated_method(self, *args, **kwargs) -> float:
        return self.decorated_method.arguments.get('first_arg')


@function_arguments(
    arg_1=Argument(
        type=str
    ),
    arg_2=Argument(
        type=(int, float),
        required=False
    )
)
def decorated_function(*args, **kwargs) -> str:
    return decorated_function.arguments.get('arg_1')