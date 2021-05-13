
import requests
from pathlib import Path
from bs4 import BeautifulSoup as bs
from page_loader.services.regexer import get_transformed_path, \
    get_transformed_filename
from urllib.parse import urlparse, urljoin


TAGS_ATTRIBUTES_MAP = {
    'img': 'src',
    'script': 'src',
    'link': 'href'
}


def alter_path(path_to_assets, url_to_alter):

    return Path(path_to_assets)


def get_and_alter_assets_pathes(html, url, path_to_assets):
    souped_page = bs(html, 'html.parser')
    assets = []

    # collect required tags from html
    tags = []
    for tag_type in TAGS_ATTRIBUTES_MAP.keys():
        tags.append(souped_page(tag_type))

    for tag in tags:
        url_to_alter = tag.get(TAGS_ATTRIBUTES_MAP[tag.name])

        if not url_to_alter:
            continue

        asset_url = urljoin(f'{url}/', url_to_alter)

        # check if the asset is internal and belong to the site
        if urlparse(asset_url).netloc != urlparse(url):
            continue

        asset_file_name = get_transformed_filename(asset_url)

        assets.append({
            'url_before_change': asset_url,
            'asset_filename': asset_file_name,
        })

        tag[TAGS_ATTRIBUTES_MAP[tag.name]] = Path(path_to_assets) / asset_file_name

    return souped_page.prettify(formatter='html5'), assets


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
