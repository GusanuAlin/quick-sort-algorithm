#Initialize a counter "comparisons" in order to count the number of comparisons
comparisons = 0
def quick_sort_pairs(arr, left, right):
    """
        The function has 3 arguments, arr, left, and right;
        arr is the array that needs to be sorted, left and right are indexes
        The function recursively calls the "partition_pairs" function
    """
    global comparisons

    if left < right:
        # recursively partition the list, and call quick_sort on the smaller lists
        partition_pos = partition_pairs(arr, left, right)
        quick_sort_pairs(arr, left, partition_pos - 1)
        quick_sort_pairs(arr, partition_pos + 1, right)


def partition_pairs(arr, left, right):
    """
    This function takes in 3 arguments, arr, left and right;
    And returns the index i after sorting the values. Arr is an array of values, while left and right are indexes;
    The function pick a pivot at right end of the array, and then finds the proper position
    of the pivot by interchanging values within the list;
    In the end the pivot is at it's proper place, and values to the left are lower and to the right are higher.
    """
    global comparisons
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        
        #Index i starts from the left of the array and moves to right until it finds a value higher than the pivot
        while i < right and arr[i][0] <= pivot[0]:
            if arr[i][0] == pivot[0]:
                if arr[i][1] < pivot[1]:
                    i += 1
                else:
                    break
            else:
                i += 1
                comparisons += 1
        
        #Index j starts from the right of the array, and moves to the left until it finds a value lower than the pivot
        while j > left and arr[j][0] >= pivot[0]:
            if arr[j][0] == pivot[0]:
                if arr[j][1] > pivot[1]:
                    j -= 1
                else:
                    break
            else:
                j -= 1
            comparisons += 1

        if i < j and arr[i][0] != arr[j][0]:
            arr[i], arr[j] = arr[j], arr[i]
        elif i < j and arr[i][0] == arr[j][0]:
            if arr[i][1] < arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

    if arr[i][0] >= pivot[0]:
        arr[i], arr[right] = arr[right], arr[i]

    return i