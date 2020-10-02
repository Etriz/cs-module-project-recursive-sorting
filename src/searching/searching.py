# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if arr == []:
        return -1

    while start <= end:
        middle = (start + end) // 2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            return binary_search(arr, target, start, middle - 1)
        elif target > arr[middle]:
            return binary_search(arr, target, middle + 1, end)
    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    if arr == []:
        return -1

    if arr[0] < arr[-1]:
        start = 0
        end = len(arr) - 1
    else:
        start = len(arr) - 1
        end = 0

    # while start <= end:
    #     middle = (start + end) // 2
    #     if target == arr[middle]:
    #         return middle
    #     elif target < arr[middle]:
    #         return agnostic_binary_search(arr, target)
    #     elif target > arr[middle]:
    #         return agnostic_binary_search(arr, target)
    return -1