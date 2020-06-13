def get_shortest_unique_substring(arr, str):
    headIndex = 0
    result = ""
    uniqueCounter = 0
    countMap = {}
    # initializing countmap
    for i in range(len(arr)):
        countMap[arr[i]] = 0

    # scan str
    for tailIndex in range(len(str)):
        tailChar = str[tailIndex]
        if not tailChar in countMap:
            continue
        tailCount = countMap[tailChar]
        if tailCount == 0:
            uniqueCounter += 1
        countMap[tailChar] = tailCount + 1
        # push head forward

        while uniqueCounter == len(arr):
            tempLength = tailIndex - headIndex + 1
            if tempLength == len(arr):
                return str[headIndex:tailIndex+1]
            if result == "" or tempLength < len(result):
                result = str[headIndex:tailIndex+1]
            headChar = str[headIndex]
            if headChar in countMap:
                headCount = countMap[headChar] - 1
            if headCount == 0:
                uniqueCounter = uniqueCounter - 1
            countMap[headChar] = headCount
            headIndex = headIndex + 1
    return result


print(get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx"))
