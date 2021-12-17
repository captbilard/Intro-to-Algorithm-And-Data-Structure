def selection_sort(list):
    """
    Set the minimum value to the first index,
    check that first index against all other elements in the list
    if none is lesser, append it to the sorted_list
    else, the lesser one is the new min and it's compared against the remaining element in the list
    """
    sorted_list = []

    for i in range(0, len(list)):
        min_index = index_of_min(list)
        sorted_list.append(list.pop(min_index))
    return sorted_list

def index_of_min(list):
    min = 0
    for i in range(1, len(list)):
        if list[i] < list[min]:
            min = i
    return min

# list = [99, 195, 108, 11, 67, 131, 125, 104, 78, 123, 92, 150, 56, 130, 36, 73, 185, 25, 159, 65, 137, 155, 38, 80, 26, 19, 85, 121, 144, 175, 91, 112, 81, 157, 164, 53, 142, 190, 114, 134, 198, 16, 141, 4, 24, 103, 1, 127, 86, 63, 84, 17, 49, 146, 57, 62, 37, 140, 115, 178, 21, 82, 194, 126, 28, 191, 75, 32, 151, 165, 74, 161, 12, 77, 154, 50, 41, 129, 31, 177, 163, 182, 106, 119, 5, 79, 173, 34, 61, 9, 152, 87, 97, 148, 20, 166, 196, 90, 70, 88]
# print(selection_sort(list))