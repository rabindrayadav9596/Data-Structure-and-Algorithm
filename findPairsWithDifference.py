def find_pairs_with_given_difference(arr, k):
    dict = {}
    result = []

    for x in arr:
        comp = x-k
        dict[comp] = x

    for y in arr:
        print(y)
        if y in dict:
            result.append([dict[y], y])
    return result


print(find_pairs_with_given_difference([4, 1], 3))
