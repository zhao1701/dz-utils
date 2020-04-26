import os
from pathlib import Path

import pytest

from dzu.path import check_path, make_directory


class TestCheckPath:

    @pytest.fixture(params=[os.getcwd(), Path(os.getcwd())])
    def make_path(self, request):
        return request.param

    @pytest.mark.parametrize('new_type', [str, Path])
    def test_to_string(self, make_path, new_type):
        path_old = make_path
        path_new = check_path(path_old, new_type)
        assert(isinstance(path_new, new_type))


class TestMakeDirectory:

    @pytest.mark.parametrize('overwrite', [True, False])
    def test_clean_make(self, tmpdir, overwrite):
        tmpdir = Path(tmpdir)
        os.removedirs(tmpdir)
        make_directory(tmpdir, overwrite=overwrite)
        assert(os.path.exists(tmpdir))

    def test_existing_make_no_overwrite(self, tmpdir):
        tmpdir = Path(tmpdir)
        with pytest.raises(FileExistsError):
            make_directory(tmpdir, overwrite=False)

    def test_existing_make_with_overwrite(self, tmpdir):
        tmpdir = Path(tmpdir)
        make_directory(tmpdir, overwrite=True)
        assert(os.path.exists(tmpdir))
