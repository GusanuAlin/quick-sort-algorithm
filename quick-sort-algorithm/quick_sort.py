#initialize a counter "comparisons" as a global variable in order to count the comparisons
comparisons = 0

def quick_sort(arr, left, right):
    """
    The function takes 3 arguments, arr, left, and right. Arr is the array that needs to be sorted, left and right are indexes.
    """
    global  comparisons
    
    if left < right:
        #recursively partition the list, and call quick_sort on the smaller lists
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)


def partition(arr,left,right):
    """
    This function takes in 3 arguments, arr, left and right. Arr is an array of values, while left and right are indexes.
    The function pick a pivot at right end of the array, and then finds the proper position of the pivot by changing values
    within the list. In the end the pivot is at it's proper place, and values to the left are lower and to the right are higher.
    """
    global comparisons
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        #Index i starts from the left of the array, and moves to right until it finds a value higher or equal than the pivot
        while i < right and arr[i] < pivot:
            comparisons += 1
            i += 1
        #Index j starts from the right of the array, and moves to the left until it finds a value lower than the pivot
        while j > left and arr[j] >= pivot:
            comparisons += 1
            j -= 1
        #Check if i is lower than j and then swap the values
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    #When i becomes bigger than j check the value at index i and than swap values
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i

