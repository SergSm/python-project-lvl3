import pytest
import requests

import os

from tempfile import TemporaryDirectory
from pathlib import Path
from urllib.parse import urljoin

from page_loader import download
from page_loader.services.names import get_transformed_filename

BASE_URL = 'https://sergsm.github.io/'
WORKING_DIR = Path(__file__).resolve().parent
FIXTURE_DIR = WORKING_DIR / 'fixtures'

HTML_FILE_NAME = 'sergsm-github-io.html'
ASSETS_DIR_NAME = 'sergsm-github-io_files'

ASSETS = [
    {
        'format': 'css',
        'url_path': 'styles.css',
        'file_name': 'sergsm-github-io-styles.css',
    },
    {
        'format': 'js',
        'url_path': 'script.js',
        'file_name': 'sergsm-github-io-script.js',
    },
    {
        'format': 'jpg',
        'url_path': '/images/sunset.jpg',
        'file_name': 'sergsm-github-io-images-sunset.jpg',
    },
]


def get_file(path_to_file, mode='r'):
    with open(path_to_file, mode) as f:
        content = f.read()
    return content


def test_network_error(requests_mock):
    bad_url = "https://shm____oogle.com"
    reference_exception = requests.exceptions.ConnectionError
    requests_mock.get(bad_url, exc=reference_exception)

    with TemporaryDirectory() as tmp_dir:
        assert not os.listdir(tmp_dir)

        with pytest.raises(reference_exception):
            assert download(bad_url, tmp_dir)

        assert not os.listdir(tmp_dir)


@pytest.mark.parametrize('code', [404])
def test_response_error(requests_mock, code):
    url = urljoin(BASE_URL, "not-real-url")
    requests_mock.get(url, status_code=code)

    with TemporaryDirectory() as tmp_dir:
        with pytest.raises(requests.exceptions.HTTPError):
            assert download(url, tmp_dir)


def test_fs_no_access_error(requests_mock):
    requests_mock.get(BASE_URL)

    some_unpermissive_path = '/bin'
    with pytest.raises(OSError):
        assert download(BASE_URL, some_unpermissive_path)


def test_fs_not_a_dir(requests_mock):
    requests_mock.get(BASE_URL)

    certainly_not_a_dir = FIXTURE_DIR / HTML_FILE_NAME
    with pytest.raises(NotADirectoryError):
        assert download(BASE_URL, certainly_not_a_dir)


def test_fs_no_such_file(requests_mock):
    requests_mock.get(BASE_URL)

    non_existance = FIXTURE_DIR / 'sdfasdfadcHTML_FILE_NAME'
    with pytest.raises(FileNotFoundError):
        assert download(BASE_URL, non_existance)


def test_download_page(requests_mock):
    html_file = get_file(FIXTURE_DIR / HTML_FILE_NAME)
    requests_mock.get(BASE_URL, text=html_file)

    html_reference_filepath = FIXTURE_DIR / HTML_FILE_NAME

    for asset in ASSETS:
        asset_url = urljoin(BASE_URL, asset['url_path'])
        reference_fs_path = FIXTURE_DIR / \
                            ASSETS_DIR_NAME / \
                            asset['file_name']
        reference_content = get_file(reference_fs_path, 'rb')
        asset['content'] = reference_content
        requests_mock.get(asset_url, content=reference_content)

    with TemporaryDirectory() as tmp_dir:

        assert not os.listdir(tmp_dir)

        print(type(requests_mock))

        #print('base_UUUURL\n'+BASE_URL)
        #print('tmp_dir\n'+tmp_dir)


        # with requests_mock.Mocker(real_http=True) as m:
        #     m.register_uri('GET', 'BASE_URL', text='resp')
        #     print(requests.get('BASE_URL').text)
        #     print(requests.get('BASE_URL').status_code)

        downloaded_html_file_path = download(BASE_URL, Path(tmp_dir).resolve())

        # assert len(os.listdir(tmp_dir)) == 2
        # assert len(os.listdir(Path(tmp_dir) / ASSETS_DIR_NAME)) == 3

        #reference_html_file_path = Path(tmp_dir) / HTML_FILE_NAME
        #assert




# def test_download_single_page():
#     url = "https://sergsm.github.io"
#
#     with TemporaryDirectory() as td:
#
#         filepath = Path(td).resolve()
#         download(url, filepath)
#
#         filename = get_transformed_filename(url)
#         with open(filepath / filename, 'r') as f:
#             result = f.read()
#             assert result == get_file(FIXTURE_DIR / filename)
#
#
# def test_download_single_page_request_mocked(requests_mock):
#     url = "https://sergsm.github.io/"
#
#     with TemporaryDirectory() as td:
#
#         filepath = Path(td).resolve()
#         filename = get_transformed_filename(url)
#
#         requests_mock.get(url, text=get_file(FIXTURE_DIR / filename))
#
#         download(url, filepath)
#
#         with open(filepath / filename, 'r') as f:
#             result = f.read()
#             assert result == get_file(FIXTURE_DIR / filename)
