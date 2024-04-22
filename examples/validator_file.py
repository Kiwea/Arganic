from arganic.validators import File

# Validation succeed
File().validate('../tests/test_dir/test_file.txt')
# Validation failure
File().validate('../tests/not_exists')