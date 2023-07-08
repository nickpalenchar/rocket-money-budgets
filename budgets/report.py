"""
Reports on spending of each category and total leftover.
The leftover can go into savings or some other big goal!
"""
import sys
import csv
from argparse import ArgumentParser
from .config import config

def main(args):

    parser = ArgumentParser(
            prog="report",
            description="generate the report from csv file"
            )

    parser.add_argument('csvfile', help='path to trasactions csv file')
    parsed = parser.parse_args(args)

    with open(parsed.csvfile) as fh:
        reader = csv.reader(fh)
        for row in reader:
            print(row)


if __name__ == '__main__':
    main(sys.argv[0])
