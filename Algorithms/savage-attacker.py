#/usr/bin/env python


# In Baldur's Gate 3, there is a feat called "Savage Attacker" that rolls your melle damage die twice and keep hte highest value.
# I know this would shift the distribution from completely equal to the right, but how much to the right?

from random import randrange

with open("savage-attacker-data.csv","a") as file:
    file.write("die-type,die-one,die-two,max\n")
    for i in range(1000):
        die_type = 6

        die_one = randrange(1,7)
        die_two = randrange(1,7)
        die_max = max(die_one,die_two)

        file.write(f"{die_type},{die_one},{die_two},{die_max}\n""")
