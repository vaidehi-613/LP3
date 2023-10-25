import random

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Partition the array into elements less than and greater than the pivot
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Recursively sort the sub-arrays
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = randomized_quick_sort(arr)
print("Sorted array:", sorted_arr)