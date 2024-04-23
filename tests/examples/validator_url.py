from arganic.validators import Url
from arganic.arguments import function_arguments, Argument


@function_arguments(
    url=Argument(
        type=str,
        validator=Url()
    )
)
def url_handler(*args, **kwargs) -> str:
    print(url_handler.arguments.get('url'))
    return url_handler.arguments.get('url')


# Validation
url_handler(url='https://www.example.com')
