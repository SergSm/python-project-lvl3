import logging as l

from pathlib import Path

from page_loader.services.regexer import get_transformed_filename, get_site_root
from page_loader.services.requester import get_response
from page_loader.services.html_handler import download_assets
from page_loader.services.html_handler import alter_img_src

CURRENT_DIR = Path.cwd()


def get_assets_dirname(filename):
    return f'{filename}_files'


def download(url, output=CURRENT_DIR):

    l.info(f"Destination url{url}")

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


###################
    if assets.Count() > 0:
        and not Path(CURRENT_DIR / assets_dirname).exists()
        CreateDIR()


    return f"The target url data has been successfully saved to " \
           f"{filepath}"
