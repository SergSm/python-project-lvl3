# TODO fs check if the dir exists

from tempfile import TemporaryDirectory
from pathlib import Path

from page_loader import download
from page_loader.services.regexer import get_transformed_filename


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


def test_download_single_page_request_mocked(requests_mock):
    url = "https://sergsm.github.io/index.html"

    with TemporaryDirectory() as td:

        filepath = Path(td).resolve()
        filename = get_transformed_filename(url)

        requests_mock.get(url, text=get_file(FIXTURE_DIR / filename))

        download(url, filepath)

        with open(filepath / filename, 'r') as f:
            result = f.read()
            assert result == get_file(FIXTURE_DIR / filename)
