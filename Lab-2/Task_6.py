# Dictionary in Python
dict1 = {
    "Cristiano" : "Ronaldo",
    "Leonel" : "Messi",
    "Real" : "Madrid",
    "year" : 2025
}

x = dict1.keys() #  keys in the dictionary
y = dict1.values() # values in dictionary
print(x)
print(y)
dict1["NBA"] = "Leykers" # update keys and values
print(x)
print(y)
z = dict1.items() # print key and value together
print(z)

if "Cristiano" in dict1: #only key
    print("Yes!!")

dict1.update({"year" : 1945})
print(z)

dict1.pop("NBA") # remove key with value
print(z)
dict1.popitem() # random item delete
print(z)

# also you can remove item with del and you can use clear(), it is remove all item
print()
print()
# Loop Dictionaries

for x in dict1:
    print(x) #print all key
    print(dict1[x]) # print all value
# also you can use .key() or .value()
print()
for x,y in dict1.items():
    print(x,y)

print()

# Copy dictionary
antherDict = dict1.copy() # also have dict() function
print(antherDict)

print()
print()

# Nested Dictionary

family = {
    "child1": {
        "name": "Almas",
        "year": 2006
    },
    "child2": {
        "name": "Nazym",
        "year": 2012
    },
    "child3": {
        "name": "Khan",
        "year": 2019
    }
}

for x, obj in family.items(): # Loop through the keys and values of all nested dictionaries
    print(x)

    for y in obj:
        print(y + ':', obj[y])
print()
print(family["child1"]["year"]) # Print the year of child 2:




