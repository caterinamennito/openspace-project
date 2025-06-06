from utils.table import Table
from utils.file_utils import file_utils
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read a file and print its contents.")
    parser.add_argument('file_path', type=str, help='Path to the file to read')
    args = parser.parse_args()
    print(f"Reading file: {args.file_path}")
    # TODO: call openspace