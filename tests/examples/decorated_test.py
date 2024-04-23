from decorated import DecoratedClass, decorated_function


class TestProperties:

    def test_default_property(self):
        dc = DecoratedClass(is_required='dfr')
        assert dc.get('int_prop') == 1

    def test_bad_type_properties(self):
        try:
            dc = DecoratedClass(int_prop='string', is_required='dfr')
        except TypeError:
            assert True
        else:
            assert False

    def test_required_properties(self):
        try:
            dc = DecoratedClass(int_prop=1)
        except ValueError:
            assert True
        else:
            assert False

    def test_bad_choice(self):
        try:
            dc = DecoratedClass(
                int_prop=1,
                is_required='dfr',
                is_choices='g'
            )
        except ValueError:
            assert True
        else:
            assert False

    def test_read_only(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a'
        )
        try:
            dc.set('is_required', 'tzu')
        except ValueError:
            assert True
        else:
            assert False

    def test_set_prop(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a'
        )
        dc.set('int_prop',2)
        assert dc.get('int_prop') == 2

    def test_set_prop_validation(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a'
        )
        try:
            dc.set('int_prop', '4')
        except TypeError:
            assert True
        else:
            assert False

    def test_set_prop_unknown(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a'
        )
        try:
            dc.set('aaa', 5)
        except KeyError:
            assert True
        else:
            assert False

    def test_is_dir(self):
        try:
            dc = DecoratedClass(
                int_prop=1,
                is_required='dfr',
                is_choices='a',
                is_dir='tests/examples/validate_dir'
            )
        except FileNotFoundError:
            assert False
        else:
            assert True


    def test_is_not_dir(self):
        try:
            dc = DecoratedClass(
                int_prop=1,
                is_required='dfr',
                is_choices='a',
                is_dir='aaa'
            )
        except FileNotFoundError:
            assert True
        else:
            assert False

    def test_is_file(self):
        try:
            dc = DecoratedClass(
                int_prop=1,
                is_required='dfr',
                is_choices='a',
                is_dir='tests/examples/validate_dir',
                is_file='tests/examples/validate_dir/validate_file.txt'
            )
        except FileNotFoundError:
            assert False
        else:
            assert True

    def test_is_not_file(self):
        try:
            dc = DecoratedClass(
                int_prop=1,
                is_required='dfr',
                is_choices='a',
                is_dir='tests/examples/validate_dir',
                is_file='fff'
            )
        except FileNotFoundError:
            assert True
        else:
            assert False

    def test_get_int_prop(selfself):
        dc = DecoratedClass(
            int_prop=99,
            is_required='dfr'
        )
        assert dc.get_int_prop() == 99


    def test_method(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/examples/validate_dir',
            is_file='tests/examples/validate_dir/validate_file.txt'
        )
        dc.decorated_method(first_arg=12.9)
        assert True

    def test_validators_length(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/examples/validate_dir',
            is_file='tests/examples/validate_dir/validate_file.txt'
        )

        try:
            dc.decorated_method(
                first_arg=15.4,
                second_arg='rrr'
            )
        except ValueError:
            assert False
        else:
            assert True

    def test_validators_wrong_min_length(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/examples/validate_dir',
            is_file='tests/examples/validate_dir/validate_file.txt'
        )

        try:
            dc.decorated_method(
                first_arg=10.3,
                second_arg='r'
            )
        except ValueError:
            assert True
        else:
            assert False

    def test_validators_wrong_max_length(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/examples/validate_dir',
            is_file='tests/examples/validate_dir/validate_file.txt'
        )

        try:
            dc.decorated_method(
                first_arg=8.7,
                second_arg='return'
            )
        except ValueError:
            assert True
        else:
            assert False

    def test_validators_email(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/examples/validate_dir',
            is_file='tests/examples/validate_dir/validate_file.txt'
        )

        try:
            dc.decorated_method(
                first_arg=2.1,
                email='test@example.com'
            )
        except ValueError:
            assert False
        else:
            assert True

    def test_validators_bad_email(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/examples/validate_dir',
            is_file='tests/examples/validate_dir/validate_file.txt'
        )

        try:
            dc.decorated_method(
                first_arg=1.7,
                email='dd@com'
            )
        except ValueError:
            assert True
        else:
            assert False

    def test_validators_url(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/examples/validate_dir',
            is_file='tests/examples/validate_dir/validate_file.txt'
        )

        try:
            dc.decorated_method(
                first_arg=45.6,
                url='https://example.com'
            )
        except ValueError:
            assert False
        else:
            assert True

    def test_validators_bad_url(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/examples/validate_dir',
            is_file='tests/examples/validate_dir/validate_file.txt'
        )

        try:
            dc.decorated_method(
                first_arg=222.7,
                url='example.com'
            )
        except ValueError:
            assert True
        else:
            assert False

    def test_method_return(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/examples/validate_dir',
            is_file='tests/examples/validate_dir/validate_file.txt'
        )
        assert dc.decorated_method(first_arg=444.5) == 444.5

    def test_function_1_return(self):
        assert decorated_function(arg_1='d') == 'd'

    def test_function_1_not_same(self):
        assert decorated_function(arg_1='d') != 'f'

    def test_function_1_type_int(self):
        decorated_function(arg_1='d', arg_2=12)
        assert True

    def test_function_1_type_float(self):
        decorated_function(arg_1='d', arg_2=12.9)
        assert True
