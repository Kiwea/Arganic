from tests.examples.custom_validator import CityValidator, drive

class CustomValidatorTest:

    def test_city_validator(self):
        if drive(start='Geneva', destination='Paris') != {'start': 'Geneva', 'destination': 'Paris'}:
            assert False
        if drive(start='Lyon', destination='Geneva') != {'start': 'Lyon', 'destination': 'Geneva'}:
            assert False
        if drive(start='Madrid', destination='Paris') != {'start': 'Madrid', 'destination': 'Paris'}:
            assert False
        assert True

    def test_city_validator_fails(self):
        try:
            drive(start='Warsaw', destination='Paris')
        except ValueError:
            assert True
        else:
            assert False
