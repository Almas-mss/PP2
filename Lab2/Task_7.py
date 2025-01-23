# If ... Else

a,b = map(int, input("Enter a and b: ").split())
if a > b:
    print("a greater than b !")
elif b > a:
    print("b greater thab a !!!")
elif a == b:
    print("a is egual to b !")

print()
print()

x = y = z = 100
if x == y  and y == z and x == z:
    print("Its alright !?")

print()
print()

h = 62
i,j = map(float, input("Enter i,j: ").split())
if i == h or j == h:
    print("Equal, Equal")
else:
    print("Hell, no")

