"""Module to clean up file names using re module"""

import re
from urllib.parse import urlparse
from pathlib import Path


def get_transformed_filename(url):

    handled_url = urlparse(url)

    relative_url = handled_url.path

    suffix = Path(relative_url).suffix

    url_no_ext = Path(relative_url).resolve().stem

    format_ = suffix if suffix else '.html'

    no_slashes_path = re.sub(r'[^0-9a-zA-Z]+',
                      '-',
                      handled_url.netloc + url_no_ext)

    result = re.sub(r'^-', '', no_slashes_path) + format_

    return result


def get_transformed_path(url):

    pattern = r"([\w_-]+[.]jpg)"

    result = re.sub()

    return re.search(pattern, url).group(0)
