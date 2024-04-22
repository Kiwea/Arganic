from arganic.validators import MaxLength

# Validation succeed
MaxLength(10).validate('example')
# Validation failure
MaxLength(1).validate('example')