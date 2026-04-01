#1.	Add few names, one name in each row, in “name.txt file”.
#a.	Count no of names
#b.	Count all names starting with vowel
#c.	Find longest name
f = open("name.txt", "w")
f.write("Anshika\nYashika\nShubhank\nPankaj")
f.close()
f = open("name.txt", "r")
names = f.read().splitlines()
print(names)
f.close()
print("Total numbers of names:", len(names))
count = 0
vowel = "AEIOUaeiou"
for name in names:
    if name[0] in vowel:
        count += 1
print("Names starting with vowel:", count)
longest_name = names[0]
for name in names:
    if len(name) > len(longest_name):
        longest_name = name

print("Longest name:", longest_name)