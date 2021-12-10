def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    
    midpoint = len(list) // 2

    if list[midpoint] == target:
        return True
    elif list[midpoint] < target:
        return recursive_binary_search(list[midpoint+1:], target)
    elif list[midpoint] > target:
        return recursive_binary_search(list[:midpoint-1], target)
    else:
        return False

def verify(result):
    print(f"Target was found: {result}")

numbers = [0,1,2,3,4,5,6,7,8,9]
result = recursive_binary_search(numbers, 15)
verify(result)
result = recursive_binary_search(numbers, 3)

verify(result)