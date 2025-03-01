text = "Hello Tony Stark"
lower = list(filter(lambda x: (x.islower()),text))
upper = list(filter(lambda x: (x.isupper()),text))
print(lower,len(lower))
print(upper,len(upper))

lower2 = sum(1 for i in text if i.islower())
upper2 = sum(1 for i in text if i.isupper())
print(lower2)
print(upper2)