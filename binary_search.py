def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first+last)// 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print(f'Target was found at index: {index}')
    else:
        print("Target wasn't found")

numbers = [1,2,3,4,5,6,7,8,9,10]

results = binary_search(numbers, 15)
verify(results)

results = binary_search(numbers, 4)
verify(results)