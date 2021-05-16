"""Module to clean up file names using re module"""

import re
from urllib.parse import urlparse
from pathlib import Path

PATTERN_ALPHA_NUMERIC = r'[^0-9a-zA-Z]+'


def get_transformed_filename(url):

    handled_url = urlparse(url)

    relative_url = handled_url.path
    suffix = Path(relative_url).suffix

    url_no_ext = str(Path(relative_url).resolve())[:-len(suffix)] \
        if relative_url else ''

    format_ = suffix if suffix else '.html'
    no_slashes_path = re.sub(PATTERN_ALPHA_NUMERIC,
                             '-',
                             handled_url.netloc + url_no_ext)

    result = re.sub(r'^-', '', no_slashes_path) + format_

    return result


def get_transformed_path(url):
    handled_url = urlparse(url)

    relative_url = handled_url.path
    suffix = Path(relative_url).suffix
    url_no_ext = str(Path(relative_url).resolve())[:-len(suffix)] \
        if relative_url else ''

    no_slashes_path = re.sub(PATTERN_ALPHA_NUMERIC,
                             '-',
                             handled_url.netloc + url_no_ext)

    no_slashes_path += '_files'

    return no_slashes_path
