import random

def problem2_4():
    random.seed(70)
    num_lis = []
    for i in range(10):
        n = (random.random() * 5 + 30)
        num_lis.append(n)
    print(num_lis)