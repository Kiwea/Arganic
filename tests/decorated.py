from arganic.properties import (
    class_properties,
    method_arguments,
    function_arguments,
    Properties,
    Property
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
    int_prop=Property(
        type=int,
        default=1,
        read_only=False
    ),
    is_required=Property(),
    is_choices=Property(
        type=str,
        choices=('a', 'b', 'c'),
        required=False
    ),
    is_dir=Property(
        type=str,
        required=False,
        validator=Dir()
    ),
    is_file=Property(
        type=str,
        required=False,
        validator=File()
    )
)
class DecoratedClass(Properties):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print(self.get('int_prop'))

    def get_int_prop(self) -> int:
        return self.get('int_prop')

    @method_arguments(
        first_arg=Property(
            type=float
        ),
        second_arg=Property(
            type=str,
            validator=(MinLength(2), MaxLength(4)),
            required=False
        ),
        email=Property(
            type=str,
            validator=Email(),
            required=False
        ),
        url=Property(
            type=str,
            validator=Url(),
            required=False
        )
    )
    def decorated_method(self, *args, **kwargs) -> float:
        return self.decorated_method.arguments.get('first_arg')


@function_arguments(
    arg_1=Property(
        type=str
    ),
    arg_2=Property(
        type=(int, float),
        required=False
    )
)
def decorated_function(*args, **kwargs) -> str:
    return decorated_function.arguments.get('arg_1')