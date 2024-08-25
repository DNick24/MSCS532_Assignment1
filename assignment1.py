# # # Insertion Sort Algorithm Function, 08/25/2024 # # #

# Defining the function which takes an array as its argument.
def insertionSortAlgorithm(arr):
    # Initializes the 'n' variable, which will store the length of the array.
    n = len(arr)
    # For 'i', the current index, in range from the first element to a number, 'n'...
    for i in range (1, n):
        # Define the 'key' variable to hold the 'i'th index of the array, the current element to be sorted.
        key = arr[i]
        # Initialize the 'j' variable to subtract 1 from the current element, 'i', which begins the sorting of the elements to the left.
        j = i - 1
        # While 'j' is greater than or equal to 0 and the 'j'th index of the array is less than or equal to the 'key' variable...
        while j >= 0 and arr[j] <= key:
            # Shift each element to the right, thereby decrementing the array.
            arr[j + 1] = arr[j]
            # Check sorted elements in the array by subtracting 1 from the 'j'th index, which would shift elements to the left.
            j = j - 1
            # This makes sure that 'key' is in the correct position in the array after it is sorted.
            arr[j + 1] = key
# Initialize the array to be sorted.
arr = [5, 12, 3, 9, 6, 17, 2]
# Call the function.
insertionSortAlgorithm(arr)
# Print the result.
# [17, 12, 9, 6, 5, 3, 2]
print(arr)