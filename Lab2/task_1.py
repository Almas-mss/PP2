# compare two values for Boolean
from operator import truediv

print( 25 > 5 ) #return T
print( 49 == 7 ) # return F
print( 16 < 4 ) # return F


# condition for Boolean
a = 100
b = 99
if b > a:
    print(" b is greater than a!")
else:
    print("a is greater than b!")

# Most values are true
x = "KBTU"
y = 21

print(bool(x))
print(bool(y))

print(bool("xyz"))
print(bool(987))
print(bool(["Almaty", "Calculus", "BMW"]))

# some values are False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myPyt():
  def __len__(self):  # _len_ returns False
    return 0

myobj = myPyt()
print(bool(myobj))


# Boolean for Functions

def myBoolean():
    return True

if myBoolean():
    print("It is True!!!")
else: print("False bro")


def myUni():
    return True
print((myUni()))


# how work isinstance

l = 333
print(isinstance(l,int))

k = "Almas"
print(isinstance(k,str))





