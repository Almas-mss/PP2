# Python arithmetic operators

a = 7
b = 2

print(("+", a + b))
print( ("-", a - b))
print( ("*",a * b))
print(( "/", a / b ))
print( ("%", a % b))
print(("**",a**b))
print(("//",a//b))

print()

# Python Assignment Operators

c = 9
c += 4

d = 8
d -= 7

e = 3
e *= 3

f = 4
f /= 2

g = 5
g %= 3

h = 19
h //= 6

i = 12
i **= 2

j = 13
j &= 4

k = 6
k |= 2

print((" += ",c))
print((" -= ",d))
print((" *= ",e))
print((" /= ",f))
print((" %= ",g))
print((" //= ",h))
print((" **= ",i))
print((" &= ",j))
print(("|=",k))

print()


# Python Comparison Operators

l = 6
m = 5
n = 6

print(l==m) # return false
print(l==n) # return True
# or can do that
print(l != m) # return True
print(l != n) # return False

print()

print(l>m) # return True
print(l>=n) #return True

print()

# Python Logical Operators

o = 15

print( o>=10 and o<=20 ) # if both statements are True
print( o>9 or o<20 ) # if only one statement is True
print(not(o>3 and o<30)) # return reverse the result

print()

# Python Identity Operators

x = ["Almaty", "City"]
y = ["Almaty", "City"]
z = x

print(x is z) # return true because is same object
print(x is y)
print(x == y) # return true because is same object

print()

# Python Membership Operators

x = ["Mussa", "Almas"]

print("Almas" in x)
print("Khan" not in x)

print()

# Operator Precedence

print( (7+3) - (2-5))
print( 200 / ( 10 + 10))





















