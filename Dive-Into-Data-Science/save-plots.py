#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

# First plot to see number of riders per hour
hours = pd.read_csv("myData.csv")

# fig is just a second object for some reason, but ax is the stuff I want
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(x=hours["instant"],y=hours["count"])

# adding labels to make the thing look nice
plt.xlabel("Hours")
plt.ylabel("Count")
plt.title("Ridership Count by Hour")

# actually save the plot
plt.savefig("ridership-count-by-hour.png",bbox_inches="tight")


# new plot count of riders per hour for first two days
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(x=hours["instant"],y=hours["count"])

plt.xlabel("Hours")
plt.xlabel("Count")
plt.title("Count by Hour - First Two Days")


plt.savefig("count-by-hour-first-two-days",bbox_inches="tight")


hour_fist48 = hours.loc[0:48,:]

fig, ax = plt.subplots(figsize=(10,6))
ax.plot(hour_fist48["instant"],hour_fist48["count"],c="blue",label="casual",linestyle="-")
ax.plot(hour_fist48["instant"],hour_fist48["registered"],c="orange",label="casual",linestyle="--")
ax.legend()

plt.xlabel("Hours")
plt.xlabel("Count & Registered")
plt.title("Count by Hour - First Two Days")
plt.savefig("count-and-registered-by-hour")
