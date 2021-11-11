

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
primes = []


for i in range(2, 100):

    if len(primes) == 10001:
        break
    x = list(map(lambda y: i % y == 0, range(2,i)))


    if sum(x) == False:
        primes.append(i)
        print(i)

print(primes[-1] , "Len: ",  len(primes))


    # x = list(map(lambda y: i % y == 0, range(2,i)))
