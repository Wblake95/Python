import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("directory")
args = parser.parse_args()
cwd = os.getcwd()
os.mkdir(cwd + "/" + args.directory)
