import argparse


parser = argparse.ArgumentParser(description='Argparse example')

parser.add_argument('numbers', type=int, help='do something with number',
                    metavar='number', nargs=3)
parser.add_argument('--flag', help='flag stored true if present',
                    action='store_true')

args = parser.parse_args()

print(f'Called with number {args.numbers} & flag {args.flag}')
