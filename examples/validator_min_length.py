from arganic.validators import MinLength

# Validation succeed
MinLength(1).validate('example')
# Validation failure
MinLength(10).validate('example')