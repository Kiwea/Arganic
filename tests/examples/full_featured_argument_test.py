from full_featured_argument import FullFeaturedArgument

class TestFullFeaturedArgument:

    def test_ffa1(self):
        # 'first' value is allowed in choices options
        ffa = FullFeaturedArgument(arg1='first')
        assert ffa.get_arg1() == 'first'

    def test_ffa2(self):
        # arg1 is not required and will take de the default value 'first'
        ffa = FullFeaturedArgument()
        assert ffa.get_arg1() == 'first'

    def test_ffa3(self):
        # arg1 can be a tuple
        ffa = FullFeaturedArgument(arg1=('first', 'second'))
        assert ffa.get_arg1() == ('first', 'second')

    def test_ffa4(self):
        # arg1 can be a tuple
        ffa = FullFeaturedArgument(arg1=['first', 'second'])
        assert ffa.get_arg1() == ['first', 'second']

    def test_not_allowed_value(self):
        # arg1 cannot be a value that not exists in choices
        try:
            ffa = FullFeaturedArgument(arg1='third')
        except ValueError:
            assert True
        else:
            assert False

    def test_set_value(self):
        ffa = FullFeaturedArgument(arg1=['first', 'second'])
        ffa.set('arg1', 'second')
        assert ffa.get_arg1() == 'second'

    def test_set_invalid_value(self):
        ffa = FullFeaturedArgument(arg1=['first', 'second'])
        try:
            ffa.set('arg1', 'third')
        except ValueError:
            assert True
        else:
            assert False

    def test_set_type_error(self):
        ffa = FullFeaturedArgument(arg1=['first', 'second'])
        try:
            ffa.set('arg1', 10)
        except TypeError:
            assert True
        else:
            assert False
