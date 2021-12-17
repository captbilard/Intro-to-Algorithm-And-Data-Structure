def split_list(list):
    """
    Split list into two halves and return both halves

    Takes 0(log n) time
    """
    midpoint = len(list) // 2
    # Slicing is an expensive operation, according to the docs it takes 0(K), where K is the size of the slicing
    left_half = list[:midpoint]
    right_half = list[midpoint:]

    return left_half, right_half


def merge(left, right):
    """
    Combines two list into one and sorts them.
    Returns the sorted list
    Takes 0(n log n)
    """
    new_list = []

    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1
    
    #IF the left list is longer than the right, the first loop would terminate, so we account for it here
    while i < len(left):
        new_list.append(left[i])
        i += 1
    
    #In case of the right list being longer

    while j < len(right):
        new_list.append(right[j])
        j += 1
    
    return new_list
    


def merge_sort(list):
    """
    Sorts a list is ascending order and returns a new list

    Divide: Divide the list into two equal halves
    Conquer: Recursively sort the sublist created above
    Combine: merge the sorted list into a new list

    Takes 0(n log n) time
    """

    # Base case for the recursive function
    if len(list) <= 1:
        return list
    
    left_half, right_half = split_list(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    #returns the sorted list
    return merge(left, right)


# Verification of sorting
def verify(list):
    """
    Checks that the list is sorted by comparing the values of the list in a recursive manner
    """

    #Base Case
    if len(list) <= 1:
        return True
    
    return list[0] < list[1] and verify(list[1:])