# arr not expected to be sorted
def simpleSearch(arr, item):
    for i in range(0, len(arr)):
        if arr[i] == item:
            return i;
    return 'not found'

print(simpleSearch([5,3,6,2,10],3))
