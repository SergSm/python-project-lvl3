"""Module to clean up file names using re"""

import re


def get_site_root(url):

    #  IN: https://sergsm.github.io/index.html
    # or
    #  IN: http://sergsm.github.io/index.html
    # or
    # https://sergsm.github.io
    #  OUT: https://sergsm.github.io/
    pattern = r"(https?:\/\/.*\/)|(https?:\/\/.*)"

    return re.search(pattern, url).group(0)


def get_transformed_filename(url):
    url_no_scheme = str(url).split('//', 1)[-1]

    pattern = r"\W"  # not a Word
    result = re.sub(pattern, "-", url_no_scheme)

    ends_wth_html = r"\b-html"
    result = re.sub(ends_wth_html, u".html", result, 0, re.MULTILINE)

    return result


def get_transformed_path(url):

    pattern = r"([\w_-]+[.]jpg)"

    result = re.sub()

    return re.search(pattern, url).group(0)
