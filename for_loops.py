friends = ["Rolf", "jen", "Anne"]

for friend in friends:
  print(friend)

print(friends)

elements = [0,1,2,3,4,5,6,7,8,9]

for index in elements:
  print(index)
  print("Hello, world !!!")


for index in range (10):
  print("Tester")

for index in range (2,10,3):
  print(index)



students = [
{"name": "X", "grade": 90},
{"name": "Y", "grade": 40},
{"name": "Z", "grade": 60},
{"name": "W", "grade": 80},
{"name": "R", "grade": 66},

]
for student in students:
  name = student ["name"]
  grade = student["grade"]

  print(f"{name} has a grade of {grade}.")