def linear_search(list, target):
    """ Returns the index where the target is located in the list"""
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f'Target was found at index: {index}')
    else:
        print("Target wasn't found")

numbers = [1,2,3,4,5,6,7,8,9,10]

results = linear_search(numbers, 15)
verify(results)

results = linear_search(numbers, 4)
verify(results)