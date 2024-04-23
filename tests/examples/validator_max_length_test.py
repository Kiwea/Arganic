from tests.examples.validator_max_length import max_len_10_handler, max_len_1_handler


class TestValidatorMaxLength():

    def test_valid_maxlength_10(self):
        assert max_len_10_handler(max_len='example') == 'example'

    def test_invalid_maxlength_10(self):
        try:
            max_len_10_handler(max_len='example,example')
        except ValueError:
            assert True
        else:
            assert False

    def test_valid_maxlength_1(self):
        assert max_len_1_handler(max_len='e') == 'e'

    def test_invalid_maxlength_1(self):
        try:
            max_len_1_handler(max_len='example')
        except ValueError:
            assert True
        else:
            assert False
