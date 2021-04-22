import pytest
import sys
from tempfile import TemporaryDirectory
from pathlib import Path
from requests_mock import mocker

#from page_loader.main import download
from page_loader import download
from page_loader.regexer import get_transformed_filename


WORKING_DIR = Path(__file__).resolve().parent
FIXTURE_DIR = WORKING_DIR / 'fixtures'


def get_file(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content


def test_download_single_page():
    url = "https://sergsm.github.io/index.html"

    with TemporaryDirectory() as td:

        filepath = Path(td).resolve()
        download(url, filepath)

        filename = get_transformed_filename(url)
        with open(filepath / filename, 'r') as f:
            result = f.read()
            assert result == get_file(FIXTURE_DIR / filename)


def test_download_single_page_request_mocked():
    url = "https://sergsm.github.io/index.html"

    with TemporaryDirectory() as td:

        filepath = Path(td).resolve()

        mocker.patch('page_loader.main.download', return_value=1)

        download(url, filepath)

        filename = get_transformed_filename(url)
        with open(filepath / filename, 'r') as f:
            result = f.read()
            assert result == get_file(FIXTURE_DIR / filename)

