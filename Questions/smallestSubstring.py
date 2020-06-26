def get_shortest_unique_substring(arr, str):
    left = 0
    result = ""
    uniqueCounter = 0
    countMap = {}
    # initializing countmap
    for i in range(len(arr)):
        countMap[arr[i]] = 0

    # scan str
    for right in range(len(str)):
        tailChar = str[right]
        if not tailChar in countMap:
            continue
        tailCount = countMap[tailChar]
        if tailCount == 0:
            uniqueCounter += 1
        countMap[tailChar] = tailCount + 1
        # push head forward

        while uniqueCounter == len(arr):
            tempLength = right - left + 1
            if tempLength == len(arr):
                return str[left:right+1]
            if result == "" or tempLength < len(result):
                result = str[left:right+1]
            headChar = str[left]
            if headChar in countMap:
                headCount = countMap[headChar] - 1
            if headCount == 0:
                uniqueCounter = uniqueCounter - 1
            countMap[headChar] = headCount
            left = left + 1
    return result


print(get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx"))
