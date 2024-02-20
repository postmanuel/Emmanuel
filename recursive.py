def recursive_search(lis, target, midpoint):
    if len(lis) == 0:
        return False
    else:
        midpoint == (len(lis)) // 2

    if lis[midpoint] == target:
        return True

    else:
        if lis[midpoint] < target:
            return recursive_search(lis[midpoint + 1:], target)
        else:
            return recursive_search(lis[:midpoint], target)


def verify(results):
    print("Target found:", results)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
res = recursive_search(numbers,9)
verify(res)
