from validator_file import file_handler


class TestValidatorFile():

    def test_valid_file(self):
        assert file_handler(file='tests/examples/validate_dir/validate_file.txt') == 'tests/examples/validate_dir/validate_file.txt'

    def test_invalid_file(self):
        try:
            file_handler(file='file/that/not/exists')
        except FileNotFoundError:
            assert True
        else:
            assert False
