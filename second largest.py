def list(numbers):
    largest = 0
    second_largest = 0

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest
numbers = [3,5,7,8,9,34,56,78]
second_largest = list(numbers)
print(second_largest)