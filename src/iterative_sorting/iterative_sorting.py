# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # arr[a], arr[b] = arr[b], arr[a]

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swap = True
    while swap == True:
        swap = False
        smallest = 0
        for i in range(smallest + 1, len(arr)):
            if arr[i] < arr[smallest]:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                swap = True
            smallest += 1
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
