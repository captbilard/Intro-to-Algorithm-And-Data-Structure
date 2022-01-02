from ten_thousand import number_value
def merge_sort(values):
    if len(values) <= 1:
        return values
    
    midpoint = len(values) // 2
    left_values, right_values = merge_sort(values[:midpoint]),merge_sort(values[midpoint:])
    sorted_values = []

    left_index, right_index = 0,0

    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    sorted_values = sorted_values + left_values[left_index:]
    sorted_values = sorted_values + right_values[right_index:]
    return sorted_values

merge_sort(number_value)