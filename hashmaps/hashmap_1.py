'''
Given an integer array nums, 
return true if any value appears more than once in the array, 
otherwise return false.

Input: nums = [1, 2, 3, 3]

Output: true

checking over array:
[1, 2, 3, 3]
 i 
    i 
       i
       False
          i True (duplicate found)

Output = True

[1, 2, 3, 4]
 i 
    i 
       i
       False
          i False (duplicate NOT found)

Output: False
'''

def contains_duplicates(nums: int, ) -> bool:
    ## Tc: O(n^2)
    ## Spc: O(n)
    ## brute force idea
    '''
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                print('True')
    print('False')
    '''
    # TC: O(n log n)
    # spc: O(n)
    nums.sort() ## O(n log n)

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            print('True') 
    print('False')

    ## [2,2,1,1,3,1,2,3,1,4]
    ##  i 
    ## i-1i
    ## [1,1,1,1,2,2,2,3,3,4]
        ## if a number in my array is equal to another nunber in my array
        ##if i[0] == i[1]
                    #i                 j
                    #0 1 2 3 4 5 6 7 8 9 --> False 
                    #  i             j
                    #0 1 2 3 4 5 6 7 8 9 --> False
                    #    i         j
                    #0 1 2 3 4 5 6 7 8 9 --> False
                    #      i     j
                    #0 1 2 3 4 5 6 7 8 9 --> False
                    #        i j
                    #0 1 2 3 4 5 6 7 8 9 --> False
                    #        j     i
                    #0 1 2 3 4 5 6 7 8 9 --> False
contains_duplicates([2,2,1,1,3,1,2,3,1,4])
    

