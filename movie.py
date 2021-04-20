def actors():
  real = input("Name: ")
  role = input("Role: ")
  return real,role


def rate_a_movie(title):
  return float(input(f"What whould you rate \'{title}\'?\n"))



def new_movie(t):
  #function to create a movie page
  movie = {}
  movie["Title"] = t
  #movie["Released"] = input("What year was it Released\n")
  movie["Genre"] = input("What genre it is ?\n")
  #movie["Duration"] = input("How long is this movie\n")
  actor_list = []
  counter = 0
  print("Provide details of the cast. How many actors are in the cast?\n")
  n=int(input())
  while counter < n:
    actor_list.append(actors())
    counter += 1
  movie["Actors"] = actor_list
  movie["Rating"] = 5.0, 0
  return movie

def movie_search(database = {}):
  print("Search by : Title, Genre or Actor?")
  opt = input()
  movie = {}
  if opt.lower() == "title":
    t = input("Enter the title: ")
    if t in database:
      movie = database[t]
    else:
      print("The database countains no info about this movie!")
  elif opt.lower() == "genre":
    g = input("Enter the genre: ")
    for details in database.values():
      if details["Genre"] == g:
        movie = details
  elif opt.lower() == "actor":
    a = input("Enter")
    for details in database.values():
      for actor in details["Actors"]:
        if actor[0] == a:
          movie = details
  return movie


def max_rated(database = {}):
  max_rating = 0
  movie = {}
  for details in database.values():
    if details["Rating"][0] > max_rating:
      max_rating = details["Rating"][0]
      movie = details
  return movie


def movie_print(movie = {}):
  print("*"*10 + " "*2 + "{}".format(movie["Title"])+ " "*2 + "*"*10)
  for item in movie.items():
    print(f"{item[0]}-----------> {item[1]}")


def imdb():
  imdb = {}
  print("Welcome to the best movie database!\n\n")
  while True:
    print("Chose an item from the menu:\n1-Add a movie\n2-Search for a movie\n3-Display all movies\n4-Get a top rated movie\n5-Rate a movie\n9-Exit")
    option = int(input())
    if option == 1:
      m_title = input("What is the title of the movie?\n")
      imdb[m_title] = new_movie(m_title)
    elif option == 2:
      print(f"Suitable movie:\n")
      movie_print(movie_search(imdb))
    elif option == 3:
      print(imdb)
    elif option == 4:
      print("You chose to find out the highest rated movie\nThis is the one:\n")
      print(max_rated(imdb))
    elif option == 5:
      print("You are rating a movie. Please be gentle")
      m = movie_search(imdb)
      current_rating = m["Rating"][0]
      number_rating = m["Rating"][1]
      x = rate_a_movie(m["Title"])
      new_rating = (number_rating * current_rating + x)/(number_rating+1)
      m["Rating"] =new_rating,number_rating+1
      imdb[m["Title"]] = m
    elif option == 9:
      break
    else:
      print("invalid option. Try again.")
  return imdb

imdb()