## Given two numbers n and r, find the value of nCr (binomial coefficient: nCr = (n!) / (r! * (n-r)!))

def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

n = int(input("enter the value of n"))
r = int(input("enter the value of r"))
fact = factorial(n)/(factorial(r)*(factorial(n-r)))
print(f'the binomial coefficient of {n} and {r} is {fact}')
