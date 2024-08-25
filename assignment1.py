def insertionSortAlgorithm(arr):
    n = len(arr)
    for i in range (2, n):
        key = arr[i]
        j = i + 1
        while j >= 0 and key >= arr[j]:
            arr[j - 1] = arr[j]
            j = j + 1
            arr[j - 1] = key
arr = [5, 12, 3, 9, 6, 17, 2]
insertionSortAlgorithm(arr)
print(arr)