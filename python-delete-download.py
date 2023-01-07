#! /bin/env python
# os mod documentation
# https://docs.python.org/3/library/os.html?highlight=os#module-os
# os.path documentation
# https://docs.python.org/3/library/os.path.html#module-os.path

import os

Home = os.path.expanduser('~')

Directory = input('What directory would you like to see? ')

print(os.listdir(f'{Home}/{Directory}'))

ToDelete = input('What would you like to delete? ')

print(os.listdir(f'{Home}/{Directory}'))

os.remove(f'{Home}/{Directory}/{ToDelete}')
