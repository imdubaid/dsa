arr = [13, 46, 24, 52, 20, 9]


def brute_force(arr):
    if not arr:
        return []

    last_elem = arr[-1]
    n = len(arr)

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last_elem

    return arr


print("Brute force: ", brute_force(arr))


def optimal(arr):
    if not arr:
        return []

    return [arr[-1]] + arr[:-1]


print("Optimal approach: ", optimal(arr))
