age = 34
#age_as_str = str(age)
#print("You are " + age)

print(f"You are {age}")

name = "Felix"
greeting = f"How are you, {name}?"
print(greeting)

name = "Bob"
print(greeting)

name = 'Felix'
final_greeting = "How are you, {}?"
felix_greeting = final_greeting.format(name)
print(felix_greeting)

name = "Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name="Jose")
print(jose_greeting)