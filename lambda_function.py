divide = lambda x, y: x / y
print(divide(15,3))

#========================
print("\nAlt program\n")
#======================

print((lambda x,y: x / y)(20,2))

#========================
print("\nAlt program\n")
#======================


def average(sequence):
  return sum(sequence) / len(sequence)


students = [
  {"name": "Rolf", "grades": (67,90,95,100)},
  {"name": "Bob", "grades": (33,93,54,10)},
  {"name": "Abba", "grades": (67,23,15,30)},
  {"name": "Ghita", "grades": (33,66,88,90)}
]

for student in students:
  print(average(student["grades"]))


#========================
print("\nAlt program\n")
#======================

average = lambda sequence: sum(sequence) / len(sequence)


students = [
  {"name": "Rolf", "grades": (67,90,95,100)},
  {"name": "Bob", "grades": (33,93,54,10)},
  {"name": "Abba", "grades": (67,23,15,30)},
  {"name": "Ghita", "grades": (33,66,88,90)}
]

for student in students:
  print(average(student["grades"])
  )