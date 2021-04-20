friend_ages = {"Rolf": 24, "Adam": 44, "Anne":21}
print(friend_ages["Rolf"])

friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25

print(friend_ages)


friends1 = (
{"name": "Rolf Smith", "age": 24},
{"name": "John ASDA", "age": 23},
{"name": "Emma Stone", "age": 44}

)

print(friends1[0]["name"])
print(friends1[1]["name"])
print(friends1[2]["name"])


friends2 = [("X", 20), ("Y", 21), ("Z", 22)]
friends2_ages = dict(friends2)
print(friends2_ages)
