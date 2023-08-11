#! /bin/env python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("1")
parser.add_argument("2")
parser.add_argument("3")

args = parser.parse_args()

print(args)
