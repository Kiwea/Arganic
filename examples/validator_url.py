from arganic.validators import Url

# Validation succeed
Url().validate('https://www.example.com')
# Validation failure
Url().validate('htp://example.com')