#! /usr/bin/env python

import requests, argparse
from os import listdir


def logic():
    # Fetching the data using the arguments
    request = requests.get(args.url)
    with open(args.filename,'w') as file:
        file.write(request.text)


# The argument parser starts
parser = argparse.ArgumentParser()
# creating arguments
parser.add_argument('url',
                    help="""URL to retrieve information.
                    Example: https://yourURL.com/thing_you_want""")
parser.add_argument('filename',
                    help="Name of the file to save as.")
# putting arguments in a variable
args = parser.parse_args()
# End arguments

# Check to make sure file types are the same, default to url filetype
if args.url[-4:] != args.filename[-4:]:
    args.filename = args.filename.replace(args.filename[-4:], args.url[-4:])

# If file already exists, ask for new name
if args.filename in listdir():
    overWrite = input("That file already exists, do you want to save over it? [y/n]: ").lower()
    if overWrite == "y":
        args.filename = args.filename.replace(args.filename[0:-4],input("new name: "))
        logic()# I see the flaw here, you could save over another file
    elif overWrite == "n":
        print("Nothing happened, closing program.")
    else:
        print("Wrong entry, closing program.")
else:
    logic()
