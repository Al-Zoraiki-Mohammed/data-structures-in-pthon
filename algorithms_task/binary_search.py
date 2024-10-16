"""Implementation of Binary Search Algorithm
"""


def binary_search(arr, key, is_sorted=False):
    """
    Implementation of Binary Search Algorithm.

    Args:
    arr (list or tuple or set): The array-like collection to be searched.
    key: The element to search for in the array.
    is_sorted (bool, optional): Indicates whether the input array is sorted. 
                                Defaults to False.

    Returns:
    int: The index of the element if found, otherwise -1.

    Note:
    If the input array is not sorted and is not a list, it will be converted to a list
    and then sorted before performing the binary search because binary search algorithm
    works only with sorted arrays:).
    """
    low = 0
    high = len(arr) - 1
    
    if not is_sorted:
        if not isinstance(arr, list):
            arr = list(arr)
        arr = sorted(arr)

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def print_result(result_, key):
    if result_ != -1:
        print(f"Element {key} is  at index: {result_}")
    else:
        print(f"Element {key} is not in the array :( ")


if __name__ == "__main__":
    arr1 = [10, 20, 30, 40, 50]
    key1 = 20
    result = binary_search(arr1, key1, is_sorted=True)
    print_result(result, key1)

    key2 = 200
    result = binary_search(arr1, key2, is_sorted=True)
    print_result(result, key2)

    arr2 = [50, 20, 10, 40, 30]
    key2 = 50
    result = binary_search(arr2, key2, is_sorted=False)
    print_result(result, key2)

    arr3 = (50, 20, 10, 40, 30)
    key3 = 10
    result = binary_search(arr3, key3)
    print_result(result, key3)

    arr4 = {50, 20, 10, 40, 30}
    key4 = 40
    result = binary_search(arr4, key4)
    print_result(result, key4)

    arr5 = {'banana', 'apple', 'pear'}
    key5 = 'apple'
    result = binary_search(arr5, key5)
    print_result(result, key5)

    arr6 = {'banana', 'apple', 'pear'}
    key6 = 'orange'
    result = binary_search(arr6, key6)
    print_result(result, key6)

    
    