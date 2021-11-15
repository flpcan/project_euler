# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.



lst = list(range(0,1000))
i=int()
j= int()
k= int()
for i in lst:
    for j in lst:
        for k in lst:
            if i + j+k ==1000 and i<j<k == True:
                print(i,j,k)
                if pow(i,2) + pow(b,2) == pow(c,2):
                    print(i,j,k)
                    
                    
                    
# Testing
