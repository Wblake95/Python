import requests

url = "https://bradfordtuckfield.com/hour.csv"

response = requests.get(url)

with open("myData.csv","wb") as file:
    file.write(response.content)
# This
