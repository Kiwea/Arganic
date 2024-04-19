from arganic.properties import (
    class_properties,
    method_arguments,
    Properties,
    Property
)
from arganic.validators import (
    File,
    Dir,
    Email,
    Url,
    MaxLength,
    MinLength
)


@class_properties(
    int_prop=Property(
        type=int,
        default=1,
        read_only=False
    ),
    is_required=Property(),
    is_choices=Property(
        type=str,
        choices=('a', 'b', 'c'),
        required=False
    ),
    is_dir=Property(
        type=str,
        required=False,
        validators=(Dir(),)
    ),
    is_file=Property(
        type=str,
        required=False,
        validators=(File(),)
    )
)
class DecoratedClass(Properties):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @method_arguments(
        first_arg=Property(
            type=float
        ),
        second_arg=Property(
            type=str,
            validators=(MinLength(2), MaxLength(4),),
            required=False
        ),
        email=Property(
            type=str,
            validators=(Email(),),
            required=False
        ),
        url=Property(
            type=str,
            validators=(Url(),),
            required=False
        )
    )
    def method_1(self, *args, **kwargs) -> None:
        pass


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
                is_dir='tests/test_dir'
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
                is_dir='tests/test_dir',
                is_file='tests/test_dir/test_file.txt'
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
                is_dir='tests/test_dir',
                is_file='fff'
            )
        except FileNotFoundError:
            assert True
        else:
            assert False

    def test_method(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/test_dir',
            is_file='tests/test_dir/test_file.txt'
        )
        dc.method_1(first_arg=12.9)
        assert True

    def test_validators_length(self):
        dc = DecoratedClass(
            int_prop=1,
            is_required='dfr',
            is_choices='a',
            is_dir='tests/test_dir',
            is_file='tests/test_dir/test_file.txt'
        )

        try:
            dc.method_1(
                first_arg=12.9,
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
            is_dir='tests/test_dir',
            is_file='tests/test_dir/test_file.txt'
        )

        try:
            dc.method_1(
                first_arg=12.9,
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
            is_dir='tests/test_dir',
            is_file='tests/test_dir/test_file.txt'
        )

        try:
            dc.method_1(
                first_arg=12.9,
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
            is_dir='tests/test_dir',
            is_file='tests/test_dir/test_file.txt'
        )

        try:
            dc.method_1(
                first_arg=12.9,
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
            is_dir='tests/test_dir',
            is_file='tests/test_dir/test_file.txt'
        )

        try:
            dc.method_1(
                first_arg=12.9,
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
            is_dir='tests/test_dir',
            is_file='tests/test_dir/test_file.txt'
        )

        try:
            dc.method_1(
                first_arg=12.9,
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
            is_dir='tests/test_dir',
            is_file='tests/test_dir/test_file.txt'
        )

        try:
            dc.method_1(
                first_arg=12.9,
                url='example.com'
            )
        except ValueError:
            assert True
        else:
            assert False
