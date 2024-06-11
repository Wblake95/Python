# /usr/bin/env python

from pathlib import Path
import os, shutil

down, doc, pics = Path.home() / "Downloads", Path.home() / "Documents", Path.home() /  "Pictures"

os.chdir(down)

checkList = os.listdir()

for i in checkList:
    match i[-4:]:
        case ".png":
            shutil.move(i, pics)
        case "jpeg":
            shutil.move(i, pics)
        case ".pdf":
            shutil.move(i, doc)
