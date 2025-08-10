## anything where I have two indices 
## slide across to the end of the array
## I'll call it Squeeze
## Squares of a Sorted array
## Squeeze doesn't add any memeory


## sorted in increasing order (might have duplicates)
## output sorted order of squares
## [-4, -1, 0, 3, 10]
## [16, 1, 0, 9, 100]

## easiest solution: sorting 
## O(n log n) time complexity

## optimized solution:
## [16, 1, 0, 9, 100]
## build  a new array --> arr =[]
## compare the left and right values
## if right is bigger than left
## append it to the array
## then move the right pointer
## ## [16, 1, 0, 9, 100]
##     L             R
##         L     R
##            R
##            L
## arr = [100, 16, 9, 1, 0]

## while L < R:
## build array

'''boiler plate
def two_pointer_template(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Do some logic involving arr[left] and arr[right]
        # Possibly move either pointer based on some condition
        
        if condition:
            left += 1
        else:
            right -= 1

    return result

'''

''' boiler plate
    left = 0
    right = len(nums) - 1
    result = []

    while left <= right:
        ## some condition
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1

        else:
            result.append(nums[right] ** 2)
            r -= 1

    result.reverse() ## inplace reversing order
    return result

    TC: O(n)
    SPC: O(n) <<-- required as part of the return
    SPC: O(1) otherwise it's o(1)
'''
