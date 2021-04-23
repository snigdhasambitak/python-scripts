#### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
    # count_primes(100) --> 25

# By convention, 0 and 1 are not prime.


def count_primes(num):
    counter = 0
    primes = []
    for n in range(2,num+1):
        prime=1
        for i in range(2,n):
            if(n%i == 0):
                prime += 1
                break
        if prime == 1:
            counter += 1
            primes.append(n)
    print(primes)
    return counter


print(count_primes(100))