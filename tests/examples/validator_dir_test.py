from validator_dir import dir_handler


class TestValidatorDir():

    def test_valid_dir(self):
        assert dir_handler(dir='tests/examples/validate_dir') == 'tests/examples/validate_dir'

    def test_invalid_dir(self):
        try:
            dir_handler(dir='directory/that/not/exists')
        except FileNotFoundError:
            assert True
        else:
            assert False
