import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("directory")
args = parser.parse_args()
os.chdir(os.path.expanduser(args.directory))
