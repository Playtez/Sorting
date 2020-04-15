# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)  # == 6 indexes
    merged_arr = [0] * elements
    # Compare the first values of each array, add smaller of the 2 to result
    # TO-DO

    for i in range(elements):
        if len(arrA) == 0 and len(arrB) > 0:
            merged_arr[i] = arrB[0]
            del arrB[0]
        elif len(arrB) == 0 and len(arrA) > 0:
            merged_arr[i] = arrA[0]
            del arrA[0]
        else:
            if arrA[0] <= arrB[0]:
                merged_arr[i] = arrA[0]
                del arrA[0]
            elif arrB[0] <= arrA[0]:
                merged_arr[i] = arrB[0]
                del arrB[0]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


arr = [2, 4, 3, 5, 1]
merge_sort(arr)

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
