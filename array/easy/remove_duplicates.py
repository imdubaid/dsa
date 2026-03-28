arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]


def brute_force(arr):
    if not arr:
        return 0

    seen = set()
    index = 0

    for num in arr:
        if num not in seen:
            seen.add(num)
            index += 1

    return index


print("Brute force: ", brute_force(arr))


def optimal(arr):
    if not arr:
        return 0

    i = 0

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1


print("Optimal approach: ", optimal(arr))
