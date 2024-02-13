def binary_search(lis, target):
    first = 0
    last = len(lis) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if lis[midpoint] == target:
            return midpoint
        elif lis[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

    # noinspection PyUnreachableCode
    def verify(index):
        if index is not None:
            print("Target found at:", index)
        else:
            print('Target not found :', index)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = binary_search(numbers, 10)
    verify(result)
