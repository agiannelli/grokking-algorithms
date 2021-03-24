# Selection Sort
# Big O: O(n^2)

# traverses entire list and returns the smallest element
# Big O: O(n)
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# for each element:
# 1. find smallest value
# 2. Remove smallest value from list
# 3. Append smallest value to new list
# 4. Repeat
# Big O: O(n)
def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest= findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))

