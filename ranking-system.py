# My Professor for the Student Investment Fund class introduced an interesting idea.
# We will evaluate fortune 500 companies on many factors that will boil down to a percentage.
# Our goal is to take that percentage (lower is better) and rank them.
# This ranking will range from 1 (lowest interest) and 5 (highest interest).
# I want to try and figure out how I can make this happen.

import random

list = [] # Create our list
for i in range(10):
    list.append(random.uniform(0.0,100.0)) # append random floats to list.
print(f"This is my data {list=}") # I just learned this, will print out the variable name and its contents.

increment = max(list)/5 # This is our lowest boundary.
print(f"This is our increment {increment=}")
rank1, rank2, rank3, rank4, rank5 = [],[],[],[],[] # creating our different lists. Could be a dict.

for i in range(len(list)): # for loop sorting out list into the appropriate list.
    if list[i] < increment:
        rank5.append(list[i]) # who we care about most. (Lowest number)
    elif increment < list[i] < increment*2:
        rank4.append(list[i])
    elif increment*2 < list[i] < increment*3:
        rank3.append(list[i])
    elif increment*3 < list[i] < increment*4:
        rank2.append(list[i])
    else:
        rank1.append(list[i]) # Everyone else goes here.
print(f"\nResults of rank1 {rank1=}")
print(f"Results of rank2 {rank2=}")
print(f"Results of rank3 {rank3=}")
print(f"Results of rank4 {rank4=}")
print(f"Results of rank5 {rank5=}")
