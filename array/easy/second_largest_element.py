arr = [13, 46, 24, 52, 20, 9]


def brute_force(arr):
    pass


print("Brute force: ", brute_force(arr))


def better(arr):
    if len(arr) < 2:
        return 0

    largest = float("-inf")
    second_largest = float("-inf")

    for elem in arr:
        largest = max(largest, elem)

    for elem in arr:
        if largest > elem > second_largest:
            second_largest = elem

    return second_largest


print("Better one: ", better(arr))


def optimal(arr):
    pass


print("Optimal one: ", optimal(arr))
