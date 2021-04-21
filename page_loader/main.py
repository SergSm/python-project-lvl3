import re
import requests

from pathlib import Path


def get_transformed_filename(url):
    url_no_scheme = str(url).split('//', 1)[-1]
    #print(url_no_scheme)
    url_no_scheme2 = url_no_scheme.split('/')
    asfasfaSFf

    info = url_no_scheme2.split('.')
    print('info')
    print(info)

    name = ""
    for bit in info:
        name += f'-{bit}'
        print(bit)

    print('±±±')
    print(name)
    print('sdfdsfsd')
    return name


def download(url, output):

    response = requests.get(url, allow_redirects=False)
    data = response.content

    name = get_transformed_filename(url)

    return name


    # with open(output) as f:
    #     f.write(data)

