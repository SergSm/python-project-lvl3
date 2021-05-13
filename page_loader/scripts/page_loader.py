import sys
import logging

from page_loader.main import download
from page_loader.cli import get_arguments


def main():

    args = get_arguments()

    logging.basicConfig(level=logging.INFO)

    try:
        print(download(args.url, args.output))
    except Exception as e:
        logging.error(e)
        sys.exit(1)

