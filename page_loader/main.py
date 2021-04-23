# TODO raise error if the output dir doesn't exist

import requests
from pathlib import Path

from page_loader.regexer import get_transformed_filename


def download(url, output):

    response = requests.get(url, allow_redirects=False)
    data = response.content
    filename = get_transformed_filename(url)

    output = Path(output).resolve()
    filepath = output / filename

    with open(filepath, 'wb') as f:
        f.write(data)

    return filepath
