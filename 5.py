
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
numbers = []
rango = list(range(1,21))

for i in range(2520,1000000000):
    x = list(map(lambda y: i % y == 0, rango))
    if all(x) == True:
        print(i)
