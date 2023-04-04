def list(numbers):

    smallest = second_smallest = None

    for num in numbers:
        if smallest is None or num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None and num != smallest:
            second_smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest

numbers = [4,3,2,1]
second_smallest = list(numbers)
print(second_smallest)


