from arganic.validators import Email
from arganic.arguments import function_arguments, Argument


@function_arguments(
    email=Argument(
        type=str,
        validator=Email()
    )
)
def email_handler(*args, **kwargs) -> str:
    print(email_handler.arguments.get('email'))
    return email_handler.arguments.get('email')


# Validation
email_handler(email='example@example.com')
