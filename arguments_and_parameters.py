def calculate_mpg():
  car= {
  "make": "Ford",
  "model": "Fiesta",
  "mileage" : 23000,
   "fuel_consumed": 460
  }

  mpg = car ["mileage"] /car["fuel_consumed"]
  name = f"{car['make']} {car['model']}"
  print(f"{name} does {mpg} miler per gallon.")

calculate_mpg()

#==================

def calculate_mpg(car_to_calculate):
  mpg = car_to_calculate ["mileage"] / car_to_calculate["fuel_consumed"]
  name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
  print(f"{name} does {mpg} miler per gallon.")

calculate_mpg({
  "make": "Ford",
  "model": "Fiesta",
  "mileage" : 23000,
   "fuel_consumed": 460
  })

  #==========================
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Audi", "model": "A6", "mileage": 33300, "fuel_consumed": 440},
    {"make": "Range", "model": "Rover", "mileage": 4000, "fuel_consumed": 640},
    {"make": "Mazda", "model": "RX-8", "mileage": 76000, "fuel_consumed": 10},
    {"make": "Mini", "model": "Cooper", "mileage": 999000, "fuel_consumed": 910},
]
def calculate_mpg(car, intro):
  print(intro)
  mpg = car["mileage"] / car["fuel_consumed"]
  name = f"{car['make']} {car['model']}"
  print(f"{name} does {mpg} miler per gallon.")

for car in cars:
  calculate_mpg(car, "New car")