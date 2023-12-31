def partition(array, low, high):  
 
    pivot = array[high]
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1
  
def quickSort(array, low, high):   
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
 
 
data = [1, 7, 4, 11, 1, 19, -32]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)


## Deterministic approach:
# Deterministic variant of quick sort algo. typically selects a pivot element in a more systematic way, such as choosing the middle as the pivot.
# time complexity : O(nlogn)
# space complexity: O(logn)
