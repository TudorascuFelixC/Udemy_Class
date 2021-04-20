cars = ["ok","ok","ok","ok","ok","ok","faulty","ok","ok","ok"]

for status in cars:
  if status == "faulty":
      print("Found faulty car, skipping..")
      break
  print(f"This car is {status}.")
  print("Shipping new car to customer!")

  

print ("\n\n\nThis is new CODE !!!!\n\n\n")



cars = ["ok","ok","ok","ok","ok","ok","faulty","ok","ok","ok"]

for status in cars:
  if status == "faulty":
      print("Found faulty car, skipping..")
      continue
  print(f"This car is {status}.")
  print("Shipping new car to customer!")