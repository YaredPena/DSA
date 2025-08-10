'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.


Thought Process: we need to return the indices of the values in our array which hold the numbers that == to the target.

Example:
        0  1  2  3
nums = [1, 2, 3, 4] target = 7
        i  j 
           i  j
              i  j

        nums[i] + nums[j] == 3 != 7
        nums[i] + nums[j] == 5 != 7
        nums[i] + nums[j] == 7 == 7 
        return [i, j]
    
    TC: O(n^2)
    SPC: O(n)
    i = nums[0]
    j = i + 1
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return nums[i]
    if len(nums) == 2:
        return [nums[i], nums[j]]

    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

    TC: O(n)
    SPC: O(n)
    i = nums[0]
    j = i + 1
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return nums[i]
    if len(nums) == 2:
        return [nums[i], nums[j]]
    
    hashmap = {}
    for index, number in enumerate(nums):
        diff = target - number
        if diff in hashmap:
            return[hashmap[diff], index]
        hashmap[number] = index
'''

def two_index_sum(nums: List[int], target: int ) -> None:
    sorted(nums) ##TC: O(n log n)

    i = 0
    j = 1