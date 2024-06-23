#/usr/bin/env python

from random import randrange

with open("savage-attacker-data.txt","a") as file:
    die_type = 6
    die_one = randrange(1,7)
    die_two = randrange(1,7)
    die_max = max(die_one,die_two)

    file.write(f"""die-type,die-one,die-two,max
    {die_type},{die_one},{die_two},{die_max}\n""")
