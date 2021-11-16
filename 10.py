
# Online Python - IDE, Editor, Compiler, Interpreter

numbers = []

for i in range(2,2000000):
    x = list(map(lambda y: i % y ==0 , range(2,i)))
    if sum(x) == False:
        numbers.append(i)
        
print(sum(numbers))
