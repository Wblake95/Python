import pandas as pd

dataFrame = pd.read_csv("hours.csv")

#print(dataFrame.head())

print("mean:\t","{:.2f}".format(dataFrame['count'].mean()))
print("std:\t","{:.2f}".format(dataFrame['count'].std()))
print("median:\t",dataFrame['count'].median())
print("min:\t",dataFrame['count'].min())
print("max:\t",dataFrame['count'].max())


print(dataFrame.describe())
