import json

with open("data/user.json", 'r') as file:
    data = json.load(file)
    print(data)
    data.append({
        "name" : "Jovan Pesic",
        "age" : 24,
        "height" : 178,
        "gender" : "male"
    })

with open("data/user.json", 'w') as file:
    json.dump(data,file,indent=4)
print(data)

