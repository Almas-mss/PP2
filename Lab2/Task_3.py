# Python lists
list1 = ["Almaty", "Paris", "Madrid"]
list2 = [1, 2, 3, 4, 5]
list3 = [False, True, False]
list4 = ["Hala", "Madrid", 15, True, False, 23, "PP2"] # a list with integers, string, boolean

print(len(list3))  # the number of items
print(list1[2])
print(list2)

print()
print()

# Access items

print(list4[1]) # second item of the list
print(list4[-1]) # last item of the list
print(list4[1:3]) # second and third item
print(list2[:4]) # from the beginning
print(list4[2:]) # from index 2 to the end
print(list4[-6:-2]) # example with negative indexes

print()

if "Hala" in list4:
    print("HALA MADRID!!!")
else:
    print("No")

print()
print()

# Change List Items

list5 = ["Real M","Barselona","Man city","Man united","Arsenal","PSG","Liverpool","Bayern"]
list5[3] = "Chelsea" #change 3rd item
print(list5)
list5[2:4] = ["Borussia", "Atletico"] #change the 2nd and 3rd item
print(list5)
list5[6:7] = ["Tottenham", "Newcastle"] # replace with two new values
print(list5)
list5[2:4] = ["Al-Nasr"]  # replace with one value
print(list5)

print()
print()

# Add list items

list5.insert(3,"Fulham") # add new value
print(list5)
list5.append("Juventus") # add new value to the end
print(list5)

list6 = ["Milan", "Inter", "Ajax","Roma"]
list5.extend(list6)
print(list5)

print()
print()

# Remove list items

list7 = ["Celtics", "Nets", "76ers","Raptors","Bulls","Heat"]
list7.remove("Bulls") # remove specific item
print(list7)
list7.pop(3) # remove specify the index
print(list7)
list7.pop() # remove last item
print(list7)
del list7[0] # del also can remove item
print(list7)
list7.clear() #clear entire the list
print(list7)

print()
print()

# Loop lists

list8 = ["TravisScott","KanyeWest","KendrickLamar","Frank Ocean","Future","Playboi Carti","AsapRocky"]
for x in list8: # print all items using for
  print(x)

print()
print()

for i in range(len(list8)): #Print all items by referring to their index number
  print(list8[i])

print()
print()

i = 0
while i < len(list8): # print all items using while
  print(list8[i])
  i +=1

print()
print()

[print(x) for x in list8] # a short hand for

print()
print()


#List Comprehension

list9 = []
for x in list8:
    if "e" in x:
        list9.append(x) #containing items with the letter "a"
print(list9)

list9 = [x for x in list8 if "s" in x] # the same but in one line
print(list9)

list9 = [x for x in list8 if x != "Future"] #Only accept items that are not "Future"
print(list9)

list9 = [x for x in range(12) if x < 7] # use the range(), accept only numbers lower than 7
print(list9)

list9 = [x.upper() for x in list8] # The new list to upper case
print(list9)

list9 = ['Lil baby' for x in list8] #the new list with item lil Baby
print(list9)

list9 = [x if x != "AsapRocky" else "YoungThug" for x in list8] #instead "asap" change on "Thug"
print(list9)

print()
print()

# Sort lists

list10 = ["Blue", "Green", "Orange","Yellow","Purple","Red","Brown"]
list10.sort() # Sort by albhabet
print(list10)

list11 = [90 , 55 , 78, 45, 100, 0 , 23, 200, 66, 96] # Sort by number
list11.sort()
print(list11)

list11.sort(reverse = True) # descending sort
list10.sort(reverse = True)
print(list11)
print(list10)

def sorting(ab):
    return (ab - 20)
list11.sort(key = sorting) # list base on how closed the number is to 20
print(list11)

list12 = ["Blue", "green", "Orange","Yellow","purple","Red","brown"]
list12.sort(key = str.lower) # capital letters being sorted before lower
print(list12)

list11.reverse()
print(list11) # reverse result

print()
print()

# Copy lists

list10 = ["Blue", "Green", "Orange","Yellow","Purple","Red","Brown"]
list13 = list10.copy() # to copy a list
print(list13)
# or you can use list()
list13 = list(list10)
print(list13)
# or you can use [:]
list13 = list10[:]
print(list13)

print()
print()

# Join lists

mylist = ["x", "y","z"]
yourlist = [9, 8, 7]
ourlist = mylist + yourlist # join two list
print(ourlist)

for x in mylist:
    yourlist.append(x) # or you can join like this
print(yourlist)

mylist.extend(yourlist) # or like this one
print(mylist)









