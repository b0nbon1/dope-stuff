def qs(arr, lo, hi):
    if lo >= hi:
        return
    pivotIdx = partition(arr, lo, hi)

    qs(arr, lo, pivotIdx - 1)
    qs(arr, pivotIdx + 1, hi)
    

def partition(arr, lo, hi):
    pivot = arr[hi]
    idx = lo - 1
    for i in range(lo, hi, 1):
        if arr[i] <= pivot:
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot
    return idx

def quickSort(arr):
    qs(arr, 0, len(arr) - 1)
    return arr

print(quickSort([2,4,6,3,1,9,5,8]))
