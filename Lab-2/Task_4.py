# Tuple

# create tuple

tuple1 = ("R1", "R2", "R3","R4","R5","R6","R7","R8")
tuple2 = ("R9",) #  tuple can be str, int, boolean

# Access Tuple Items
print(tuple1[1])
print(tuple1[-1])
print(tuple1[2:5])
print(tuple1[:6])
print(tuple1[3:])
print(tuple1[-4:-1])
if "R7" in tuple1:
    print("Yes!!!")

print()
print()

# Change item in tuple

mylist = list(tuple1)
mylist[1] = "L2"  # You can convert the tuple into a list
print(mylist)

anotherList = list(tuple1)
anotherList.append("L9")  # add new item in tuple
tuple1 = tuple(anotherList)
print(tuple1)

tuple1+=tuple2 # add new item with help another tuple
print(tuple1)

anotherTuple = tuple2 * 3 # multiply items by 3
print(anotherTuple)

print()

# Unpack Tuple

tuple3 = ("Math","PP2","Physics","Chemistry")
(green, red, yellow, purple) = tuple3  # unpacking
print(green)
print(red)
print(yellow)
print(purple)

print()

(P1,P2,*P3) = tuple3 # P3 is rest in tuple3
print(P1)
print(P2)
print(P3)

print()

(K1, *K2, K3) = tuple3
print(K1)
print(K2)
print(K3)

print()

# Loop tuples

for x in tuple1: # items by using a for loop.
    print(x)

print()

for i in range(len(tuple3)):  # Print all items by referring to their index number
    print(tuple3[i])

print()

i = 0
while i< len(tuple1): # # items by using a While
    print(tuple1[i])
    i+=1

