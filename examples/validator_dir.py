from arganic.validators import Dir

# Validation succeed
Dir().validate('../tests/test_dir')
# Validation failure
Dir().validate('../tests/not_exists')