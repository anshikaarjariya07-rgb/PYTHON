'''1.	Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ):
Example:
Dehradun 5.78 308.20
Delhi 190 1484
……………
Open file city.txt and read to:
a.	Display details of all cities
b.	Display city names with population more than 10Lakhs
c.	Display sum of areas of all cities'''
cities = []

# Read file
with open("city.txt", "r") as f:
    for line in f:
        name, population, area = line.split()
        cities.append((name, float(population), float(area)))

# a. Display details of all cities
print("Details of all cities:")
for city in cities:
    print(city[0], city[1], city[2])

# b. Cities with population > 10 lakhs
print("\nCities with population more than 10 lakhs:")
for city in cities:
    if city[1] > 10:
        print(city[0])

# c. Sum of all areas
total_area = sum(city[2] for city in cities)
print("\nTotal area of all cities:", total_area)