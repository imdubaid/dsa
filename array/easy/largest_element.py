arr = [13, 46, 24, 52, 20, 9]


def method_one(arr):
    if len(arr) == 0:
        return 0

    largest = arr[0]
    for elem in arr:
        largest = max(largest, elem)

    return largest


print("Method one: ", method_one(arr))


def method_two(arr):
    if len(arr) == 0:
        return 0

    largest = float("-inf")
    for elem in arr:
        largest = max(largest, elem)

    return largest


print("Method two: ", method_two(arr))
