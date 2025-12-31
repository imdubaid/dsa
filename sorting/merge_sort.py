input = [13, 46, 24, 52, 20, 9]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    left = merge_sort(left_part)
    right = merge_sort(right_part)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print("Merge sort: ", merge_sort(input))
