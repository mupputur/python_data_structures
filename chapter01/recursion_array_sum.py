


def rescursion_sum_list(x):
    if len(x) == 0:
        return 0
    else:
        return rescursion_sum_list(x[1:]) + x[0]



print(rescursion_sum_list([1, 2, 3, 4, 5, 6]))