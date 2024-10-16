"""implement the bubble sort algorithm to sort an array (list, tuple, or set)
 ascending  or descending.
"""


def bubble_sort(arr, is_descending=False):
    """
    implement the bubble sort algorithm to sort an array (list, tuple, set).

    Args:
    - arr (list, tuple, or set): The array to be sorted.
    - is_descending (bool): When True the algorithm sorts descending.
            default: (False) sorts ascending.

    Returns:
    list: The sorted array.
    """
    if not isinstance(arr, list):
        arr = list(arr)

    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(0, arr_length-i-1):
            if is_descending:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == "__main__":
    arr1 = [22, 96, 2, 1, 2, 67, 68, 25, 17, 5, 31]

    sorted_arr = bubble_sort(arr1)
    print(f'Ascending: {sorted_arr}')

    sorted_arr = bubble_sort(arr1, True)
    print(f'Descending: {sorted_arr}')

    arr2 = [100_000, 123, 129_450, -193, 972, -59, 3]
    sorted_arr = bubble_sort(arr2)
    print(f'Ascending: {sorted_arr}')

    sorted_arr = bubble_sort(arr2, True)
    print(f'Descending: {sorted_arr}')

    arr3 = [-23, 98, 0, -3, -5, 145, 2.5]
    sorted_arr = bubble_sort(arr3)
    print(f'Ascending: {sorted_arr}')

    sorted_arr = bubble_sort(arr3, True)
    print(f'Descending: {sorted_arr}')

    arr_set = {5, 0, 4, 3, 2, 1}
    sorted_arr = bubble_sort(arr_set)
    print(f'Ascending: {sorted_arr}')

    sorted_arr = bubble_sort(arr_set, True)
    print(f'Descending: {sorted_arr}')

    arr_tuple = (5, 0, 4, 3, 2, 1)
    sorted_arr = bubble_sort(arr_tuple)
    print(f'Ascending: {sorted_arr}')

    sorted_arr = bubble_sort(arr_tuple, True)
    print(f'Descending: {sorted_arr}')
