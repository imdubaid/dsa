arr = [13, 46, 24, 52, 20, 9]


def is_array_sorted(arr):
    if len(arr) <= 1:
        return True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


print("Is Array Sorted: ", is_array_sorted(arr))
