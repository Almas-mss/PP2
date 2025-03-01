# Access Set Items

set1 = {"Almaty", "Astana", "Shymkent"}

for x in set1:
  print(x)

print("Astana" in set1)
print("Turkistan" not in set1)

print()
print()

# Add items

set1.add("Kyzylorda") # to add one item to a set
print(set1)

set2 = {"Washington", "Paris","Berlin"}
set1.update(set2) #To add items from another set
print(set1)

# can be another object like tuple, list and so on

lisst = ["KBTU","AITU","NU"]
set1.update(lisst)
print(set1)

print()
print()

# Remove Set Items

set1.remove("Astana") # also discard() can delete item
print(set1)

x = set1.pop() # can remove a random item
print(x)
print(set1)

set1.clear() # remove all items
print(set1)

print()
print()

# Join sets
set3 = {10, 11, 12, 13, 14}
set4 = {"x", "y", "z"}
set5 = set3.union(set4)
print(set5) # also you can use set3 = set1 | set2

set6 = {"KBTU", "NU", "NARXOZ","ALMAU","AUES"}
set7 = {"SDU","KAZNU","MNU","KBTU","MUIT","NU"}
set8 = set6.intersection(set7) # also you can use set8 = set6 & set6 instead intersection()
print(set8) # only dublicates

set6.intersection_update(set7) # there is no need to create another set
print(set6)

set6 = {"KBTU", "NU", "NARXOZ","ALMAU","AUES"}
set9 = set6 - set7 # new set that will contain only the items from the first set that are not present in the other set
print(set9) # also you can use difference()

myset = set6.symmetric_difference(set7) # you can use ^ instead
print(myset)






