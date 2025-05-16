import random

random_list = [random.randint(0, 99) for i in range(100)]
print(random_list)

No_duplicate_set=set(random_list)
print(No_duplicate_set)