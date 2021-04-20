is_learning = True

while is_learning:
    print("You're learning")
    user_input = input("Are you still learning?\n")
    is_learning = user_input == "yes"

#==================


user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
      print("we're running !!")
      user_input = input("Do you with to run the program? (yes/no): ")
print("we stopped running")
