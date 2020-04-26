from pathlib import Path

import pytest

from file_io import *


@pytest.fixture
def data_dict():
    data = {
        'job': 'composer',
        'name': {'first': 'Jerry', 'last': 'Goldsmith'},
        'films': [
            'Star Trek', 'Rambo', 'Total Recall', 'Mulan', 'The Mummy']}

@pytest.fixture
def text_lines():
    lines = [
        'Jerry Goldsmith\n',
        'Thomas Newman\n',
        'James Newton Howard\n',
        'John Powell\n']
    return lines


class TestJSON:

    def test_write_read_json(self, tmpdir, data_dict):
        tmpdir = Path(tmpdir)
        path = tmpdir / 'test.json'
        write_json(path, data_dict)
        read_dict = read_json(path)
        assert(read_dict == data_dict)


class TestYAML:

    def test_write_read_yaml(self, tmpdir, data_dict):
        tmpdir = Path(tmpdir)
        path = tmpdir / 'test.json'
        write_yaml(path, data_dict)
        read_dict = read_yaml(path)
        assert(read_dict == data_dict)


class TestText:

    def test_write_read_text(self, tmpdir, text_lines):
        tmpdir = Path(tmpdir)
        path = tmpdir / 'test.txt'
        write_text(path, text_lines)
        read_lines = read_text(path)
        assert(read_lines == text_lines)
