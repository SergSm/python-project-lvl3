
import requests
from pathlib import Path
from bs4 import BeautifulSoup as bs
from page_loader.services.regexer import get_transformed_path


def download_assets(site_root, html_content, assets_dirname):
    """Download all the assets in a  *_filesfolder
    returns a list of filenames"""

    assets_dirname = Path(assets_dirname).resolve()

    soup = bs(html_content, 'html.parser')
    tag = 'img'

    imgs_tags = soup.find_all(tag)
    urls = [img['src'] for img in imgs_tags]

    for url in urls:
        filename = get_transformed_path(url[1:])

        data = requests.get(f'{site_root}{url[1:]}')
        with open(assets_dirname / filename, 'wb') as f:
            f.write(data)


def alter_img_src(html):
    # TODO """Changes pathes to images to local"""

    return html   # TODO remove stub
