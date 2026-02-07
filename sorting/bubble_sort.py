arr = [13, 46, 24, 52, 20, 9]


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n == 1:
        return arr

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return recursive_bubble_sort(arr, n - 1)


print("Bubble sort: ", bubble_sort(input))
print("Recursive bubble sort: ", recursive_bubble_sort(input.copy()))
