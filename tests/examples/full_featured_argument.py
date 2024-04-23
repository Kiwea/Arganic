from arganic.arguments import Argument, class_properties, ArgumentHandler  # Import Argument class.
from arganic.validators import MinLength, MaxLength  # Import validators


# Argument example
@class_properties(
    arg1=Argument(
        type=(str, list, tuple),  # Multiple types are supported.
        required=False,  # This argument is not required.
        default='first',  # A default value.
        read_only=False,  # This Argument/property is not writeable.
        choices=('first', 'second', ['first', 'second'], ('first', 'second')),  # Available choices.
        validator=(MinLength(1), MaxLength(10))  # Validators.
    )
)
class FullFeaturedArgument(ArgumentHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_arg1(self) -> str | list | tuple:
        return self.get('arg1')


# 'first' value is allowed in choices options
ffa1 = FullFeaturedArgument(arg1='first')
print(ffa1.get_arg1())

# arg1 is not required and will take de the default value 'first'
ffa2 = FullFeaturedArgument()
print(ffa2.get_arg1())

# arg1 can be a tuple
ffa3 = FullFeaturedArgument(arg1=('first', 'second'))
print(ffa3.get_arg1())

# arg1 can be a list
ffa4 = FullFeaturedArgument(arg1=['first', 'second'])
print(ffa4.get_arg1())

# arg1 can be set
ffa4 = FullFeaturedArgument(arg1=['first', 'second'])
print(ffa4.get_arg1())
ffa4.set('arg1', 'second')
print(ffa4.get_arg1())
