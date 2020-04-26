from inspect import signature, _empty

import numpy as np


def check_iterable(arg, expected_length):
    """
    Checks whether an iterable `arg` is of `expected_length.` If `arg` is
    not an iterable, it is broadcast and converted into one of
    `expected_length`.

    Returns
    -------
    arg : tuple of length `expected_length`
    """
    singleton_types = (int, float, str, bool)
    iter_types = (tuple, list, np.ndarray)
    if isinstance(arg, singleton_types):
        arg = (arg,) * expected_length
    elif isinstance(arg, iter_types):
        assert(
            len(arg) == expected_length),\
            'Length of <arg> does not match expected length.'
    else:
        raise TypeError('arg is incorrect type')
    return arg


def check_iterables(*args):
    """
    Checks that all iterable arguments have the same length and converts all
    non-iterable arguments to a length consistent with that of iterable
    arguments.

    Returns
    -------
    tuple where all elements are iterables of consistent length
    """
    iter_args = [
        arg for arg in args
        if hasattr(arg, '__len__')
        and not isinstance(arg, str)]
    expected_length = 1
    if len(iter_args) > 0:
        for iter_arg in iter_args:
            if len(iter_arg) != len(iter_args[0]):
                raise ValueError('Length of iterable args does not match.')
        expected_length = len(iter_args[0])
    return tuple(check_iterable(arg, expected_length) for arg in args)


def get_function_args(fn, *args, **kwargs):
    """
    Given a function with its default arguments, a set of positional and
    keyword arguments to be passed to said function, returns a dictionary of
    the resulting parameter, argument pairs.

    Returns
    -------
    metadata : dict
        Keys are parameter names and values are arguments
    """
    # Convert tuple of positional parameters to dictionary
    arg_names = list(signature(fn).parameters.keys())
    args_ = dict(zip(arg_names[:len(args)], args))

    # Create metadata dict with default values
    metadata = {
        arg: None if param.default is _empty else param.default
        for arg, param in signature(fn).parameters.items()}

    # Update metadata dict with positional and keyword parameters
    metadata.update(args_)
    metadata.update(kwargs)
    return metadata
