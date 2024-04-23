from arganic.arguments import (
    class_properties,
    method_arguments,
    Argument,
    ArgumentHandler
)


@class_properties(
    name=Argument(
        type=str,
    ),
    type=Argument(
        type=str,
        choices=('car', 'truck', 'bike'),
        default='car'
    ),
    description=Argument(
        type=str,
        required=False
    ),
)
class Vehicle(ArgumentHandler):
    """
    A class that manage Vehicles.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_properties(self) -> dict:
        print(self.values) # Validated values
        return self.values

    @method_arguments(
        start=Argument(
            type=str
        ),
        destination=Argument(
            type=str
        )
    )
    def drive(self, *args, **kwargs) -> dict:
        """
        Drive the vehicle
        """
        print(self.drive.arguments.values) # Validated values
        return self.drive.arguments.values


car_1 = Vehicle(name="Red car")
car_1.drive(start='Geneva', destination='Paris')
bike_1 = Vehicle(name="Yellow bike", type="bike")
bike_1.drive(start='Lyon', destination='Geneva')
truck_1 = Vehicle(name="Blue truck", type="truck", description="Very heavy truck.")
truck_1.drive(start='Madrid', destination='Paris')
