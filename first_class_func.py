def greet():
  print("Hello")

#greet()

hello = greet
hello()

#=================
print("\nalt progrm\n")
#=================

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
  {"name": "Rolf", "grades": (67,90,95,100)},
  {"name": "Bob", "grades": (33,93,54,10)},
  {"name": "Abba", "grades": (67,23,15,30)},
  {"name": "Ghita", "grades": (33,66,88,90)}
]


for student in students:
  name = student["name"]
  grades = student["grades"]
  
  print(f"Student: {name}")
  operation = input("Enter 'average', 'total', or 'top': ")
  
  if operation == "average":
    print(avg(grades))
  elif operation == "total":
    print(total(grades))
  elif operation == "top":
    print(top(grades))


#=================
print("\nalt progrm\n")
#=================


avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
  "average" : avg,
  "total" : total,
  "top" : top
}
students = [
  {"name": "Rolf", "grades": (67,90,95,100)},
  {"name": "Bob", "grades": (33,93,54,10)},
  {"name": "Abba", "grades": (67,23,15,30)},
  {"name": "Ghita", "grades": (33,66,88,90)}
]


for student in students:
  name = student["name"]
  grades = student["grades"]
  
  print(f"Student: {name}")
  operation = input("Enter 'average', 'total', or 'top': ")
  
  operation_function = operations[operation]