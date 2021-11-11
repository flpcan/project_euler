
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
list = []
pal = []

for i in range(100,1000):
    for z in range(100,1000):
        number  = i * z
        list.append(number)


for num in list:
    if str(num) == str(num)[::-1]:
        pal.append(num)

print(max(pal))
