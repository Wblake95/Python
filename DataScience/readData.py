import pandas as pd

dataFrame = pd.read_csv("hours.csv")

#print(dataFrame.head())

#print("mean:\t","{:.2f}".format(dataFrame['count'].mean()))
#print("std:\t","{:.2f}".format(dataFrame['count'].std()))
#print("median:\t",dataFrame['count'].median())
#print("min:\t",dataFrame['count'].min())
#print("max:\t",dataFrame['count'].max())
#
#print(dataFrame.describe())
#
#print(dataFrame.loc[2:4,"registered"])


#print(dataFrame.loc[dataFrame["hr"]<5,"registered"].mean())
#print(dataFrame.loc[dataFrame["hr"]<5,"registered"].describe())

#print("{:.2f}".format(dataFrame.loc[(dataFrame["hr"]<5) & (dataFrame["temp"]<0.50),"count"].mean()),"\n")
#print(dataFrame.loc[(dataFrame["hr"]<5) & (dataFrame["temp"]<0.50),"count"].describe())

#print(dataFrame.groupby(["season"])["count"].mean())

print(dataFrame.groupby(["season","holiday"])["count"].mean())
