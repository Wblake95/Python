import argparse, qrcode, datetime
date = str(datetime.date.today()) + ".png"
print(date)

parser = argparse.ArgumentParser()
parser.add_argument("link")
parser.add_argument("-f","--filename", default=date)

args = parser.parse_args()

img = qrcode.make(args.link)
type(img)
print(args)
img.save(args.filename)
