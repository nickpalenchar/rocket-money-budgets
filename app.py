from argparse import ArgumentParser
import sys
import budgets


def main(args):
    parser = ArgumentParser(
            prog='rocket-report',
            description='generate reports from rocket money trasactions')
    parser.add_argument('command')
    parser.add_argument('argv', nargs='*')

    args = parser.parse_args()

    if args.command == 'report':
        print('oing')
        print(args.argv)
        budgets.report.main(args.argv)
    print(args)
    print(args.argv)

if __name__ == '__main__':
    main(sys.argv)
