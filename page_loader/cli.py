import os
import argparse


def get_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--output',
        help="local path to save the downloaded data",
        default=os.getcwd()
    )

    args = parser.parse_args()

    return args
