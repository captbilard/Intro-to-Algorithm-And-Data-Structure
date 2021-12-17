import random

def is_sorted(list):
    if len(list) <= 1:
        return True
    return list[0] < list[1] and is_sorted(list[1:])

def bogo_sort(list):
    """
    This sorting algorithm randomly shuffles the list in place
    till it is sorted.
    """
    attempts = 0
    while not is_sorted(list):
        print(attempts)
        random.shuffle(list)
        attempts += 1
    return list

list = [23,43,12,1,45,64]

print(is_sorted(list))
x = bogo_sort(list)

print(x)