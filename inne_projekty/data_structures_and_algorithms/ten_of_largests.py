import random

numbers = []
for i in range(100):
    m = random.randint(1,500)
    numbers.append(m)

n = 10

largests = []
while n>0:
    max = 0
    for i in range(len(numbers)):
        if numbers[i] >= max:
            max = numbers[i]
    numbers.remove(max)
    largests.append(max)
    n -= 1

print(largests)


                
    
