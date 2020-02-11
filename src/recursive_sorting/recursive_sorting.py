# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    aIndex = 0
    bIndex = 0
    mIndex = 0

    while aIndex < len(arrA) and bIndex < len(arrB):
        if arrA[aIndex] <= arrB[bIndex]:
            merged_arr[mIndex] = arrA[aIndex]
            aIndex += 1
            mIndex += 1
        else:
            merged_arr[mIndex] = arrB[bIndex]
            bIndex += 1
            mIndex += 1

    while(aIndex < len(arrA)):
        merged_arr[mIndex] = arrA[aIndex]
        aIndex += 1
        mIndex += 1
    while(bIndex < len(arrB)):
        merged_arr[mIndex] = arrB[bIndex]
        bIndex += 1
        mIndex += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        middle = int(len(arr)/2)
        left = arr[:middle]
        right = arr[middle:]
        return merge(merge_sort(left), merge_sort(right))
    else:
        return arr


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
