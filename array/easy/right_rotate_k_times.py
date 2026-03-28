arr = [13, 46, 24, 52, 20, 9]


def brute_force(arr, k):
    if not arr or not k:
        return

    n = len(arr)
    rotations = k % n

    for _ in range(rotations):
        el = arr.pop()
        arr.insert(0, el)

    return arr


print("Brute force: ", brute_force(arr, 3))
