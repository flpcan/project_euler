# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

lst = list(range(0,1000))
numbers = []
finals= []
i=int()
j= int()
k= int()
for i in lst:
    for j in range(0,1000):
        for k in range(0,1000):
            if i+j+k == 1000:
                numbers.append([i,j,k])
for i in numbers:
    if i[0] < i[1] and i[1] < i[2]:
        finals.append(i)
print(finals)
for i in finals:
    last = pow(i[0],2) + pow(i[1],2)
    if last == pow(i[2],2):
        print("Final :",i)
