class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in numMap:
                    return[numMap[diff], index]
            numMap[value] = index