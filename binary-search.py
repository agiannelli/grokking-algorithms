# Binary Search
# Big O: O(log n)

# assumption: array is already sorted
# establish 3 variables:
#   - low, to signify the lower bound
#   - high, to signify the upper bound
#   - mid, the "guess" we are making
# if term at middle (guess) equals
# our search term we're done
# if search term is greater than
# our guess, update low to be mid + 1
# if search term is lower than
# our guess, update high to be mid - 1
def binarySearch(arr, term):

    print('%s%s' % ('Term: ', term))
    turns = 0
    low = 0
    high = len(arr) - 1
    while(low <= high):
        turns+=1
        mid = (low + high) // 2
        guess = arr[mid]
        if term == guess:
            print('Found!')
            return ('%s%s' % ('Number of turns: ', turns))
        if term > guess:
            low = mid + 1
        else:
            high = mid -1       
    return 'not found'

print(binarySearch([1,2,3,4,5,6,7,8,9,10],7))
