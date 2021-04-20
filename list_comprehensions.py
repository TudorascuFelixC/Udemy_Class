numbers = [0,1,2,3,4,5]
doubled_numbers = []

for numer in numbers:
  doubled_numbers.append(numbers * 2)

print(doubled_numbers)

print("\nvar usoara\n")

doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

print("\nAlta varianta\n")

doubled_numbers = [number * 2 for number in range(5)]
print(doubled_numbers)

#===============

friend_ages = [22,31,35,37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

print(age_strings)

#=======
friend = input("Enter your name: ")
friends = ["Rolf", "Bob", "Jen", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
  print(f"{friend} is one of your friends")
  print(f"{friend.titlecased} is one of your friends") #.title sa scrie doar cu prima litera mare