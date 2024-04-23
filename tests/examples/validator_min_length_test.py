from validator_min_length import min_len_1_handler, min_len_10_handler


class TestValidatorMinLength():

    def test_valid_minlength_10(self):
        assert min_len_10_handler(min_len='example1234') == 'example1234'

    def test_invalid_minlength_10(self):
        try:
            min_len_10_handler(min_len='example')
        except ValueError:
            assert True
        else:
            assert False

    def test_valid_minlength_1(self):
        assert min_len_1_handler(min_len='example') == 'example'

    def test_invalid_minlength_1(self):
        try:
            min_len_1_handler(min_len='')
        except ValueError:
            assert True
        else:
            assert False
