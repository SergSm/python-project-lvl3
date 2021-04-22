"""Module to clean up file names using re"""

import re


def get_transformed_filename(url):
    url_no_scheme = str(url).split('//', 1)[-1]

    pattern = r"\W"  # not a Word
    result = re.sub(pattern, "-", url_no_scheme)

    ends_wth_html = r"\b-html"
    result = re.sub(ends_wth_html, u".html", result, 0, re.MULTILINE)

    return result
