from page_loader.main import download
from page_loader.cli import get_arguments


def download():

    args = get_arguments()
    print(download(args.save_to))