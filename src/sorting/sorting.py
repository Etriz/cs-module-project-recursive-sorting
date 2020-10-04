# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    #! Your code here
    # as long as both arrays have something in them
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)
            merged_arr.pop(0)
        else:
            merged_arr.append(arrB[0])
            arrB.pop(0)
            merged_arr.pop(0)
    # if either array is empty before the other
    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        arrA.pop(0)
        merged_arr.pop(0)
    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB.pop(0)
        merged_arr.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    #! Your code here
    # just return the arr if length is 0 or 1
    if len(arr) > 1:
        # find middle point
        middle = len(arr) // 2
        # split arr into 2  parts
        left = arr[:middle]
        right = arr[middle:]

        # merge sort on left then on right
        left = merge_sort(left)
        right = merge_sort(right)

        # merge 2 halfs back together
        sorted_array = merge(left, right)
        return sorted_array
    # return arr is no sort is needed
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
