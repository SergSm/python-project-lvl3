"""Module to clean up file names using re module"""

import re
from urllib.parse import urlparse
from pathlib import PurePath


def get_transformed_filename(url):

    handled_url = urlparse(url)

    relative_url = handled_url.path

    url_no_ext = PurePath(relative_url).stem
    suffix = PurePath(relative_url).suffix

    format_ = suffix if suffix else '.html'

    no_slashes_path = re.sub(r'^[a-zA-Z0-9_]*$',
                      '-',
                      handled_url.netloc + url_no_ext)

    result = re.sub(r'^-', '', no_slashes_path) + format_

    return result


def get_transformed_path(url):

    pattern = r"([\w_-]+[.]jpg)"

    result = re.sub()

    return re.search(pattern, url).group(0)
