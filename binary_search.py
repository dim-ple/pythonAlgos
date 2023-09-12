
# This function takes in an array, a value that we'd like to find in our array (our target),
# our starting index (which is default is 0), and end index (which is defaulted to the
# length of the array minus 1). The function then returns the index at which the value is
# found with a time complexity of O(log n). This function will use recursion.
def binarySearch(arr, target, start=0, end=len(arr)-1):

    # Checks to see if the starting index is larger than the end index.
    # If this condition is true, we know that we reached the end of our array
    # and the value was not found. This is one of two base cases included in our
    # function.
    if start > end:
        print("Target is not contained within the array")
        return -1

    # Initialize the middle index of the argument array
    # the middle index is rounded to the nearest interger using
    # the built-in round() function
    MIDDLE_INDEX = round((start + end) / 2)


    # Checking the value associated with the middle index of the array,
    # we our base case confirms we've found the the target value
    if arr[MIDDLE_INDEX] == target:
        print(f"Target value {target} found at Index {MIDDLE_INDEX}")
        return MIDDLE_INDEX

    # If the value associated with the middle index of our array is
    # greater than the target value, we call the function again and update
    # our ending index by assigning the end argument a value of the middle
    # index minus 1, effectively cutting the array in half and then searching
    # for the target value again.
    if arr[MIDDLE_INDEX] > target:
        return binarySearch(arr, target, start, MIDDLE_INDEX-1)

    # If the value associated with the middle index of our array is less than
    # the target value, we call the function again. We update the starting index argument
    # by assigning it a value of the middle index value plus 1. 
    if arr[MIDDLE_INDEX] < target:
        return binarySearch(arr, target, MIDDLE_INDEX+1, end)


