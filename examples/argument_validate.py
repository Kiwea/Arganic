from arganic.arguments import Argument  # Import Argument class.
from arganic.validators import MinLength, MaxLength  # Import validators


# Argument example
Argument(
    type=(str, list, tuple),  # Multiple types are supported.
    required=False,  # This argument is not required.
    default='default',  # A default value.
    read_only=False,  # This Argument/property is not writeable.
    choices=('default', ['first', 'second'], ('fist', 'second')),  # Available choices.
    validator=(MinLength(1), MaxLength(10))  # Validators.
).validate(['first', 'second'])  # Value validation.
