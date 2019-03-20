import os
from shutil import rmtree
from pathlib import Path


def make_directory(path, overwrite=False, verbose=True):
    if isinstance(path, Path):
        path = path.resolve().as_posix()
    elif not isinstance(path, str):
        raise ValueError('Input must be a path-like object.')

    if os.path.isdir(path) and not overwrite:
        raise FileExistsError('Directory already exists.')
    elif os.path.isdir(path) and overwrite:
        if verbose:
            print('{} already exists. Overwriting ...'.format(path))
        rmtree(path)

    os.makedirs(path)
    
