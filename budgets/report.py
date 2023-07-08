"""
Reports on spending of each category and total leftover.
The leftover can go into savings or some other big goal!
"""
import sys
import csv
from decimal import *
from argparse import ArgumentParser, BooleanOptionalAction
from collections import defaultdict
from pprint import pprint
from .config import config

BUDGET_CATEGORIES = [
        'Coffee',
        'Entertainment & Rec',
        'Dining & Drinks',
        'Auto & Transport',
        'Groceries',
        'Health & Wellness',
        'Shopping',
        'Fitness'
        ]

# total for all the budget categories
BUDGET_LIMIT = 500 + 525 + 615 + 300 + 225 + 120 + 300 

CARYOVER_CATEGORIES = [
        'Travel & Vacation',
        'Discretionary',
        ]


def main(args):

    parser = ArgumentParser(
            prog="report",
            description="generate the report from csv file"
            )

    parser.add_argument('csvfile', help='path to trasactions csv file')
    parser.add_argument('--include-ignored', default=False, action=BooleanOptionalAction)
    parsed = parser.parse_args(args)

    with open(parsed.csvfile) as fh:
        reader = csv.DictReader(fh)
        categories = defaultdict(int)

        raw_total = Decimal(0)
        budget_totals = Decimal(0)
        caryover_totals = Decimal(0)

        for row in reader:
            if not parsed.include_ignored and row['Ignored From']:
                print('ignoring a transaction')
                continue
            amount = Decimal(row['Amount'])
            categories[row['Category']] += amount
            raw_total += amount
            if row['Category'] in BUDGET_CATEGORIES:
                budget_totals += amount
            if row['Category'] in CARYOVER_CATEGORIES:
                caryover_totals += amount

        
        for category, amount in categories.items():
            print(f'{category}: {amount}')

        budget_spent = BUDGET_LIMIT - budget_totals
        print(f'RAW TOTAL: {raw_total}')
        print(f'BUDGET TOTAL: {budget_totals}')
        print(f'CARYOVER TOTAL: {caryover_totals}')
        print(f'REMANING BUDGET: {budget_spent}')

if __name__ == '__main__':
    main(sys.argv[0])
