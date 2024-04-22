from arganic.arguments import class_properties, Argument, ArgumentHandler


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
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print(self.get('name'))
        print(self.get('type'))
        print(self.get('description'))


car_1 = Vehicle(name="Red car")
bike_1 = Vehicle(name="Yellow bike", type="bike")
truck_1 = Vehicle(name="Blue truck", type="truck", description="Very heavy truck.")