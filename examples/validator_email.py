from arganic.validators import Email

# Validation succeed
Email().validate('example@example.com')
# Validation failure
Email().validate('this is not an email address')