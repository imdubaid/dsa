num = int(input("Enter a number: "))
text = input("Enter a text: ")


def print_number(n, curr=1):
    if curr > n:
        return
    print(curr)
    print_number(n, curr + 1)


def print_number_reverse(n):
    if n == 0:
        return
    print(n)
    print_number_reverse(n - 1)


def sum_of_numbers(n, sum=0):
    if n == 0:
        return
    sum += n
    return sum_of_numbers(n - 1, sum)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def reverse_array(arr):
    def reverse(arr, start, end):
        if start >= end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        reverse(arr, start + 1, end - 1)

    reverse(arr, 0, len(arr) - 1)


def is_palindrome(text, i=0):
    if i >= len(text) // 2:
        return True

    if text[i] != text[len(text) - i - 1]:
        return False

    return is_palindrome(text, i + 1)


def fibonacci_series(n):
    second_last = 0
    last = 1
    series = [second_last, last]
    for i in range(2, n + 1):
        curr = second_last + last
        series.append(curr)
        second_last = last
        last = curr
    return series


arr = [1, 2, 3, 4, 5]
print("Printing numbers from 1 to", num, "is", print_number(num))
print("Printing numbers from", num, "to 1 is", print_number_reverse(num))
print("Sum of numbers from 1 to", num, "is", sum_of_numbers(num))
print("Factorial of", num, "is", factorial(num))
reverse_array(arr)
print("Reversed array is", arr)
print("Is palindrome", is_palindrome(text))
print("Fibonacci series of", num, "is", fibonacci_series(num))
