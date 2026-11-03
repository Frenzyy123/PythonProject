import json
from methods import load_file,save_file
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

save_file("data/user.json","Teca")

