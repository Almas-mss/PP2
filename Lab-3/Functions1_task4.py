numbers = list(map(int,input("Enter numbers: ").split()))

def filter_prime():
    isPrime = lambda n: n > 1 and all(n % i !=0 for i in range(2,n))
    primeNums = list(filter(isPrime, numbers))
    print(primeNums)
filter_prime()