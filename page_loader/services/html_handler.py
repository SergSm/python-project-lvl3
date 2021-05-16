import requests

from pathlib import Path
from bs4 import BeautifulSoup as bs
from page_loader.services.names import get_transformed_filename
from urllib.parse import urlparse, urljoin
from progress.bar import Bar


TAGS_ATTRIBUTES_MAP = {
    'img': 'src',
    'script': 'src',
    'link': 'href'
}

ASSET_CHUNK_SIZE = 128


def alter_path(path_to_assets, url_to_alter):

    return Path(path_to_assets)


def get_and_alter_assets_pathes(html, url, path_to_assets):
    souped_page = bs(html, 'html.parser')
    assets = []

    tags = [*souped_page('script'),
            *souped_page('link'),
            *souped_page('img')]

    for tag in tags:
        url_to_alter = tag.get(TAGS_ATTRIBUTES_MAP[tag.name])

        if not url_to_alter:
            continue

        asset_url = urljoin(f'{url}/', url_to_alter)

        # check if the asset is internal and belong to the site
        if urlparse(asset_url).netloc != urlparse(url).netloc:
            continue

        asset_file_name = get_transformed_filename(asset_url)

        assets.append({
            'url': asset_url,
            'filename': asset_file_name,
        })

        tag[TAGS_ATTRIBUTES_MAP[tag.name]] = Path(path_to_assets) / asset_file_name

    return souped_page.prettify(formatter='html5'), assets


def download_assets(assets, path_to_assets):
    """Download all the assets in a  *_filesfolder
    returns a list of filenames"""

    for asset in assets:
        response = requests.get(asset['url'], stream=True)

        full_local_path = str(Path(path_to_assets) / asset['filename'])
        with open(full_local_path, 'wb') as f:
            content_length = int(response.headers.
                                 get('content-length', '0'))

            chunks_amount = (content_length / ASSET_CHUNK_SIZE) + 1

            with Bar(full_local_path, max=chunks_amount) as progress_bar:
                for chunk in response.\
                        iter_lines(chunk_size=ASSET_CHUNK_SIZE):
                    f.write(chunk)
                    progress_bar.next()
