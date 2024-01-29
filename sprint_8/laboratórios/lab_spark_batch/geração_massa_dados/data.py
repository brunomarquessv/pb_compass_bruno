import random

num_list = [random.randint(0, 1000) for _ in range(250)]

num_list.reverse()
print(num_list)
