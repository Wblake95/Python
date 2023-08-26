# from os import path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("toDelete")
args = parser.parse_args()
os.remove(args.toDelete)
