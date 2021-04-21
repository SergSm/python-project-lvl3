import os
import argparse


def get_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('url')

    parser.add_argument(
        '-o',
        '--output',
        help="local path to save the downloaded data",
        default=os.getcwd(),
    )

    args = parser.parse_args()

    return args
