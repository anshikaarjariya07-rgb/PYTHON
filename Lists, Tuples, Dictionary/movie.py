#5.	Store details of n movies in a dictionary by taking input from the user. 
# Each movie must store details like name,  year, director name, 
# production cost, collection made (earning) & perform the following :-
#a)	print all movie details
#b)	display name of movies released before 2015
#c)	print movies that made a profit.
#d)	print movies directed by a particular director.
n = int(input("Enter number of movies: "))

movies = {}

# Input movie details
for i in range(n):
    name = input("\nEnter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    cost = float(input("Enter production cost: "))
    collection = float(input("Enter collection made: "))
    
    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

# a) Print all movie details
print("\nAll Movie Details:")
for name, details in movies.items():
    print(name, ":", details)

# b) Movies released before 2015
print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

# c) Movies that made profit
print("\nMovies that made profit:")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)

# d) Movies by particular director
search_director = input("\nEnter director name to search: ")

print("Movies directed by", search_director, ":")
for name, details in movies.items():
    if details["director"].lower() == search_director.lower():
        print(name)