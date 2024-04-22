from arganic.arguments import function_arguments, Argument

@function_arguments(
    start=Argument(
        type=str
    ),
    destination=Argument(
        type=str
    )
)
def drive(*args, **kwargs) -> None:
    print('Drive')
    print('start', drive.arguments.get('start'))
    print('destination', drive.arguments.get('destination'))


drive(start='Geneva', destination='Paris')
drive(start='Lyon', destination='Geneva')
drive(start='Madrid', destination='Paris')