from validator_email import email_handler


class TestValidatorEmail():

    def test_valid_email(self):
        assert email_handler(email='example@example.com') == 'example@example.com'

    def test_invalid_email(self):
        try:
            email_handler(dir='not_an_email')
        except ValueError:
            assert True
        else:
            assert False
