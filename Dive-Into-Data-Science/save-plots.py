#! /usr/bin/env python

import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

# First plot to see number of riders per hour
hours = pd.read_csv("myData.csv")
#
## fig is just a second object for some reason, but ax is the stuff I want
#fig, ax = plt.subplots(figsize=(10,6))
#ax.scatter(x=hours["instant"],y=hours["count"])
#
## adding labels to make the thing look nice
#plt.xlabel("Hours")
#plt.ylabel("Count")
#plt.title("Ridership Count by Hour")
#
## actually save the plot
#plt.savefig("ridership-count-by-hour.png",bbox_inches="tight")
#
#
## new plot count of riders per hour for first two days
#fig, ax = plt.subplots(figsize=(10,6))
#ax.scatter(x=hours["instant"],y=hours["count"])
#
#plt.xlabel("Hours")
#plt.xlabel("Count")
#plt.title("Count by Hour - First Two Days")
#
#
#plt.savefig("count-by-hour-first-two-days",bbox_inches="tight")
#
#
#hour_fist48 = hours.loc[0:48,:]
#
#fig, ax = plt.subplots(figsize=(10,6))
#ax.plot(hour_fist48["instant"],hour_fist48["count"],c="blue",label="casual",linestyle="-")
#ax.plot(hour_fist48["instant"],hour_fist48["registered"],c="orange",label="casual",linestyle="--")
#ax.legend()
#
#plt.xlabel("Hours")
#plt.xlabel("Count & Registered")
#plt.title("Count by Hour - First Two Days")
#plt.savefig("count-and-registered-by-hour")


#fig, ax = plt.subplots(figsize=(10,6))
#sns.boxplot(x="hr",y="registered",data=hours)
#plt.xlabel("Hour")
#plt.ylabel("Registered")
#plt.title("Registered by Hour")
#
#plt.savefig("registered-by-hour-seaborn.png")
#plt.show()


#colVars = ["hr", "temp", "windspeed"]
#first100Hours = hours.loc[0:100, colVars]
#sns.pairplot(first100Hours, corner=True)
#plt.savefig("sns-pairplot-hr-temp-windspeed")
#plt.show()


#fig, ax = plt.subplots(figsize=(10,6))
#plt.scatter(x=hours["temp"],y=hours["hum"],c="blue")
#plt.xlabel("Humidity")
#plt.ylabel("Tempature")
#plt.title("Scatter Plot Test, Hum v. Temp")
#plt.savefig("scatter-plot-test-hum-tmp")
#plt.show()


fig, ax = plt.subplots(figsize=(10,6))
plt.scatter(x=hours["casual"],y=hours["registered"],c="blue")
plt.xlabel("Casual")
plt.ylabel("Registered")
plt.title("Correlation Scatter for Registered and Casual r={:.2f}".format(hours["registered"].corr(hours["casual"])))
plt.savefig("correlation-scatter-reg-v-cas")
plt.show()
