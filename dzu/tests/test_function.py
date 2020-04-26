import pytest
import numpy as np

from dzu.function import check_iterable, check_iterables, get_function_args


class TestCheckIterable:

    @pytest.mark.parametrize('arg', [1, 1.0, '1', True])
    @pytest.mark.parametrize('length', range(1, 6))
    def test_singleton(self, arg, length):
        assert((arg,) * length == check_iterable(arg, length))

    @pytest.mark.parametrize('arg_type', [list, tuple])
    @pytest.mark.parametrize('length', range(1, 5))
    def test_iterable(self, arg_type, length):
        data = arg_type(np.random.randn(length))
        result = check_iterable(data, length)
        assert(isinstance(result, arg_type) and len(result) == length)

    def test_type_error(self):
        with pytest.raises(TypeError):
            check_iterable(None, 5)

    @pytest.mark.parametrize('length', range(2, 5))
    def test_incorrect_length(self, length):
        with pytest.raises(AssertionError):
            check_iterable(np.random.randn(length), length+1)


class TestCheckIterables:

    def test_all_singletons(self):
        a, b, c, d = True, 1, 1.0, '1'
        assert(((a,), (b,), (c,), (d,)) == check_iterables(a, b, c, d))

    def test_mix(self):
        a, b, c, d = True, [1, 2, 3], 1.0, '1'
        assert(all(len(x) == 3 for x in check_iterables(a, b, c, d)))

    @pytest.mark.parametrize('l', range(1, 6))
    def test_all_iterables(self, l):
        a, b, c, d = [True] * l, list(range(l)), [1.0] * l, ['1'] * l
        a_, b_, c_, d_ = check_iterables(a, b, c, d)
        assert(a_ == a and b_ == b and c_ == c and d_ == d)

    def test_error(self):
        a, b, c, d = True, [1, 2, 3], [1.0], '4'
        with pytest.raises(ValueError):
            check_iterables(a, b, c, d)


class TestGetFunctionArgs:

    @pytest.fixture
    def function(self):
        def f(a, b, c=2, d=3):
            pass
        return f

    def test_no_args(self, function):
        result = {'a': None, 'b': None, 'c': 2, 'd': 3}
        assert(get_function_args(function) == result)

    def test_all_args(self, function):
        result = {'a': 0, 'b': 1, 'c': -2, 'd': -3}
        assert(get_function_args(function, 0, 1, c=-2, d=-3) == result)

    def test_all_positional(self, function):
        result = {'a': 0, 'b': 1, 'c': -2, 'd': -3}
        assert(get_function_args(function, 0, 1, -2, -3) == result)

    def test_all_keyword(self, function):
        result = {'a': 0, 'b': 1, 'c': -2, 'd': -3}
        assert(get_function_args(function, d=-3, a=0, b=1, c=-2) == result)
