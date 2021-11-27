# CLI, argparse
import sys

# params = sys.argv
# print(f"Hello, {params[1]}!", params)

from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("first_word", type=str, default='')
args.add_argument("second_word", type=str, default='')
# args.add_argument("--age", type=int, default=42, help="Введи целое число")
# args.add_argument("-f", "--flag", type=bool, default=True)
args = vars(args.parse_args())
# print(args)
print(f"Hello, {args['first_word']}, {args['second_word']}!")