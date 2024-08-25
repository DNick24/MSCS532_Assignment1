# Test commit
def insertionSortAlgorithm(arr):
    array = [5, 12, 3, 9, 6, 17, 2]
    for i in range (2, n):
        key = A[i]
        j = i - 1
        while j < 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
            A[j + 1] = key
    print(key)