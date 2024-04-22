from arganic.arguments import method_arguments, Argument


class Vehicle():

    @method_arguments(
        start=Argument(
            type=str
        ),
        destination=Argument(
            type=str
        )
    )
    def drive(self, *args, **kwargs) -> None:
        print('Drive')
        print('start', self.drive.arguments.get('start'))
        print('destination', self.drive.arguments.get('destination'))


car_1 = Vehicle()
car_1.drive(start='Geneva', destination='Paris')
bike_1 = Vehicle()
bike_1.drive(start='Lyon', destination='Geneva')
truck_1 = Vehicle()
truck_1.drive(start='Madrid', destination='Paris')