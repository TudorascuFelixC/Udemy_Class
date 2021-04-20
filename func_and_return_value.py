cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Audi", "model": "A6", "mileage": 33300, "fuel_consumed": 440},
    {"make": "Range", "model": "Rover", "mileage": 4000, "fuel_consumed": 640},
    {"make": "Mazda", "model": "RX-8", "mileage": 76000, "fuel_consumed": 10},
    {"make": "Mini", "model": "Cooper", "mileage": 999000, "fuel_consumed": 910},
]

def calculate_mpg(car):
  mpg = car["mileage"] / car["fuel_consumed"]
  return mpg


def car_name(car):
  name = f"{car['make']} {car['model']}"
  return name


def print_car_info(car):
  name = car_name(car)
  mpg = calculate_mpg(car)

  print(f"{name} does {mpg} miler per gallon.")


for car in cars:
   print_car_info(car)


#====================
print("\nAsta e alt program\n")
#====================

def divide(x,y):
  if y == 0:
    return "You tried to divide by 0!"
  else:
    return x / y

print(divide(10,2))
print(divide(6,0))