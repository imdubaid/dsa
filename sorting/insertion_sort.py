arr = [13, 46, 24, 52, 20, 9]


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        prevIndex: int = i - 1

        while prevIndex >= 0 and arr[prevIndex] > key:
            arr[prevIndex + 1] = arr[prevIndex]
            prevIndex -= 1

        arr[prevIndex + 1] = key
    return arr


def recursive_insertion_sort(arr, n=0):
    if n == len(arr):
        return arr

    key = arr[n]
    prevIndex = n - 1

    while prevIndex >= 0 and arr[prevIndex] > key:
        arr[prevIndex + 1] = arr[prevIndex]
        prevIndex -= 1

    arr[prevIndex + 1] = key
    return recursive_insertion_sort(arr, n + 1)


print("Insertion sort: ", insertion_sort(input))
print("Recursive insertion sort: ", recursive_insertion_sort(input.copy()))
