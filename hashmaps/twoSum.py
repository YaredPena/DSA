class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = dict()
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numMap:
                    return[numMap[diff], i]
            numMap[n] = i