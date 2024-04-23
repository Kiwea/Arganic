from tests.examples.validator_url import url_handler


class TestValidatorUrl:

    def test_valid_url(self):
        assert url_handler(url='https://www.example.com') == 'https://www.example.com'

    def test_invalid_url(self):
        try:
            url_handler(url='not_an_url')
        except ValueError:
            assert True
        else:
            assert False
