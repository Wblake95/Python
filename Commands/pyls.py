import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("directory")
args = parser.parse_args()
list = os.listdir(os.path.expanduser(args.directory))
list.sort()
for i in range(len(list)):
    print(list[i])
