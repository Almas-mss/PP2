numbers = [1,2,3,4,5,6,7,8,9]

oddsq = list(map(lambda  x: x**2,filter(lambda x:x%2==1,numbers)))
print(oddsq)