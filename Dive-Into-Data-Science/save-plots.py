import pandas as pd
import matplotlib.pyplot as plt


hours = pd.read_csv("myData.csv")

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(x=hours["instant"],y=hours["count"])

plt.xlabel("Hours")
plt.ylabel("Count")
plt.title("Ridership Count by Hour")


plt.savefig("ridership-count-by-hour.png",bbox_inches="tight")
