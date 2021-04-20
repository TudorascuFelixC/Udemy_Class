friends = ["Rolf", "bob", "Anne"]
friends1 = [["X",21], ["Y",44], ["Z", 26]]
print(friends[0])
print(friends[1])
print(friends1[0][1])
print(friends1[1][1])

print(len(friends))


friends2 = [
  ["A",23],
  ["B", 24],
  ["C",25],
  ["D",26],
  ["E",27],
  ["F",28],
]

friends2.append(["G",29])
friends2.remove(["C",25])
print(friends2)