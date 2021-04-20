cars = ["ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping..")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")

else:
  print("All cars built succesfully. No faulty cars!")