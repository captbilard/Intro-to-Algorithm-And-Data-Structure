def quicksort(values):
    """
        This sorts by picking a pivot, then seperatin the list into 2, left side contains 
        values less than or equal to pivot, right side values > pivot.
        Then it does this recursively.
    """
    # Set stop clause for your recursion
    if len(values) <= 1:
        return values
    # Get the Pivot
    pivot = values[0]

    left, right = [],[]
    # loop of the remaining part of the lop and sort
    for value in values[1:]:
        if value <= pivot:
            left.append(value)
        else:
            right.append(value)
    return quicksort(left) + [pivot] + quicksort(right)

