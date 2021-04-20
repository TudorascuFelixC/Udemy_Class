def actors():
  real = input("Name: ")
  role = input("Role: ")
  return real,role

def new_movie():
  #function to create a movie page
  movie = {}
  movie["Title"] = input("What is the Title?\n")
  movie["Released"] = input("What year was it Released\n")
  movie["Genre"] = input("What genre it is ?\n")
  movie["Duration"] = input("How long is this movie\n")
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
  if option.lower() == "title":
    t = input("Enter the title: ")


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
      break
    elif option == 3:
      break
    elif option == 4:
      break
    elif option == 5:
      break
    elif option == 9:
      break
    else:
      print("invalid option. Try again.")
    return imdb
print(imdb())