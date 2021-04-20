truthy = True
falsy = False

age = 20
is_over_age = age >= 18
is_under_age = age <= 18
is_twenty = age == 20
print(is_over_age)
print(is_under_age)
print(is_twenty)


my_number = 5
user_number = int(input("Enter a number: "))
matches = my_number == user_number
print(my_number == user_number)
print(f"You got it right: {matches}.")