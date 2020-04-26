import os
import shutil
from pathlib import Path


def check_path(path, path_type=str):
    """
    Checks that a path is a valid path and converts it to a target type.

    Parameters
    ----------
    path : pathlib.Path, str, or list of such objects
    path_type : type, one of str or pathlib.Path
        The desired type to convert `path` into

    Returns
    -------
    Converted path of type `path_type` or list of converted paths.
    """
    if isinstance(path, path_type):
        return path
    elif isinstance(path, (list, tuple)):
        paths = path.copy()
        paths = [check_path(path, path_type=path_type) for path in paths]
        return paths
    elif path_type == str:
        path = path.as_posix()
        return path
    elif path_type == Path:
        path = Path(path)
        return path
    else:
        raise ValueError(
            'Path checking only supports pathlib.Path or str types.')


def make_directory(path, overwrite=False):
    """
    Makes a new directory.

    Parameters
    ----------
    path : str or pathlib.Path
    overwrite : bool
    """
    path = check_path(path, path_type=str)
    if os.path.isdir(path):
        if overwrite is False:
            raise FileExistsError
        else:
            shutil.rmtree(path)
    os.makedirs(path)
