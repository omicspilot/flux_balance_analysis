import requests

url = "http://bigg.ucsd.edu/static/models/iML1515.json"
response = requests.get(url)

with open("models/iML1515.json", "wb") as f:
    f.write(response.content)

print("Model downloaded and saved as models/iML1515.json")
