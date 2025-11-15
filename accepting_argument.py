# import sys
# name=sys.argv[1:]
# print(f'Hello {name}')

import argparse
parser=argparse.ArgumentParser(
    description='This program prints the name of the dogs'
)

parser.add_argument('-c','--color',metavar='color',required=True,choices={'red','yellow'})

args=parser.parse_args()
print(args.color)