import requests
import logging as l

from pathlib import Path

from page_loader.services.names import get_transformed_filename
from page_loader.services.requester import get_response
from page_loader.services.html_handler import get_and_alter_assets_pathes, \
    download_assets
from page_loader.services.html_handler import alter_img_src

CURRENT_DIR = Path.cwd()


def get_assets_dirname(filename):
    return f'{filename}_files'


def extract_assets_info():
    pass


def download(url, output_dir=CURRENT_DIR):

    l.info(f"Destination url {url}")

    # set up file names and directories pathes
    output_dir = Path(output_dir).resolve()
    filename = get_transformed_filename(url)
    assets_dirname = get_assets_dirname(filename)

    path_to_file = output_dir / filename
    path_to_assets = output_dir / assets_dirname

    l.info(f"saving to {output_dir}")

    response = get_response(url)

    html, assets = get_and_alter_assets_pathes(response.content,
                                               url,
                                               path_to_assets)

    with open(path_to_file, 'w') as f:
        l.info(f'html file save to {path_to_file}')
        f.write(html)

    if len(assets) > 0:
        if not Path(path_to_assets).exists():
            l.info(f'Creating new assets dir at {path_to_assets}')
            Path(path_to_assets).mkdir()

        download_assets(assets, path_to_assets)

    return f"The target url data has been successfully saved to " \
           f"{output_dir}"
