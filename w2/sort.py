import random

numbers=[]
for _ in range(9000):
    numbers.append(random.randint(1,2000))


print(numbers)

print(sorted(numbers))
numbers.sort()
print(numbers)

print(sorted(numbers, reverse=True))
numbers.sort(reverse=True)
print(numbers)

