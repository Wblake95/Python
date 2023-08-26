import argparse, qrcode, datetime, requests
# from os import path
date = str(datetime.date.today())

parser = argparse.ArgumentParser()
parser.add_argument("link")
parser.add_argument("-f","--filename", default=date)
parser.add_argument("-l","--location", default=date)

args = parser.parse_args()
try:
    r = requests.head(args.link, allow_redirects=True)
except:
    print("That is not a valid url")
if r.status_code == 200:
    img = qrcode.make(args.link)
    type(img)
    img.save(args.filename + ".png")
elif r.status_code == 404:
    print("That is not a valid url")
