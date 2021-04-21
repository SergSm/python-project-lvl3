from page_loader.main import download
from page_loader.cli import get_arguments


def main():

    args = get_arguments()
    print(download(args.output, args.url))
