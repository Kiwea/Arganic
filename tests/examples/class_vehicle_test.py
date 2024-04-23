from class_vehicle import Vehicle


class TestVehicle:

    def test_vehicle_1(self) -> None:
        vehicle = Vehicle(name="Red car")
        if vehicle.get_properties() != {'name': 'Red car', 'type': 'car', 'description': None}:
            assert False
        if vehicle.drive(start='Geneva', destination='Paris') != {'start': 'Geneva', 'destination': 'Paris'}:
            assert False
        assert True

    def test_vehicle_2(self) -> None:
        vehicle = Vehicle(name="Yellow bike", type="bike")
        if vehicle.get_properties() != {'name': 'Yellow bike', 'type': 'bike', 'description': None}:
            assert False
        if vehicle.drive(start='Lyon', destination='Geneva') != {'start': 'Lyon', 'destination': 'Geneva'}:
            assert False
        assert True

    def test_vehicle_3(self) -> None:
        vehicle = Vehicle(name="Blue truck", type="truck", description="Very heavy truck.")
        if vehicle.get_properties() != {'name': 'Blue truck', 'type': 'truck', 'description': "Very heavy truck."}:
            assert False
        if vehicle.drive(start='Madrid', destination='Paris') != {'start': 'Madrid', 'destination': 'Paris'}:
            assert False
        assert True
