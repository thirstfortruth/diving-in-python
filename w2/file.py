import random 
num_list = []

for _ in range(10):
    num_list.append(random.randint(1,30))


str_list = list(map(str, num_list))

for num in num_list:
    print(type(num))

for st in str_list:
    print(type(st))
