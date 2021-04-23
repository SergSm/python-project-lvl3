# TODO raise error if the output dir doesn't exist

from pathlib import Path

from page_loader.services.regexer import get_transformed_filename, get_site_root
from page_loader.services.requester import get_response
from page_loader.services.html_handler import download_assets
from page_loader.services.html_handler import alter_img_src

CURRENT_DIR = Path.cwd()


def get_assets_dirname(filename):
    return f'{filename}_files'


def download(url, output=CURRENT_DIR):

    filename = get_transformed_filename(url)
    assets_dirname = get_assets_dirname(filename)
    site_root = get_site_root(url)

    response = get_response(url)
    data = {
        'html': response.content,
        'assets': download_assets(site_root,
                                  response.content,
                                  assets_dirname)
    }

    data['html'] = alter_img_src(data['html'],
                                 data['assets'])

    output = Path(output).resolve()
    filepath = output / filename

    with open(filepath, 'wb') as f:
        f.write(data)

    return filepath
