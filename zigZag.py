#!/usr/bin/env python

import time, sys

try:
    indent=0
    wave='********'
    gainLoss=True
    increaseIndent=True
    while increaseIndent:
        if gainLoss:
            indent+=1
            print(' '*indent,wave)
            time.sleep(0.1)
            gainLoss=False if indent==5 else True
        else:
            indent-=1
            print(' '*indent,wave)
            time.sleep(0.1)
            gainLoss=True if indent==0 else False
except KeyboardInterrupt:
    sys.exit()
