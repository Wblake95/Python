#! /usr/bin/env python

import requests

request = requests.get('https://bradfordtuckfield.com/hour.csv')

with open('hours.csv','w') as file:
    file.write(request.text)

