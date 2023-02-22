import json

with open("sample-data.json") as f:
    data = json.load(f)

for person in data:
    name = person["first_name"] + " " + person["last_name"]
    age = person["age"]
    email = person["email"]
    phone = person["phone"]
    print(f"Name: {name}, Age: {age}, Email: {email}, Phone: {phone}")