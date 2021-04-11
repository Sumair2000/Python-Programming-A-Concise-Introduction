def problem1_3(n):
    my_sum = 0
    while my_sum <= n:
        my_sum = sum(range(n+1))
    print(my_sum)