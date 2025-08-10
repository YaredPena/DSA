'''
this is an unoptimized solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## we're making this to check for frequency
        hashmap = {} 

        ##print(len(nums))

        ## I can iterate over the array and begin to store 
        ## the frequency of each number
        ## value, frequency
        ## {2: 2, 3: 3}
        for i in range(len(nums)): 
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        ##print(nums[i])
        ## after checking the frequencies of each number
        ## i should return the most frequent number(s)
        ## i need to check for the most frequent number then after
        ## that I need to return the nth most frequent numbers dependent
        ## on how many numbers k is looking for.

        ## note this is sorting in descended order
        ## I realize now I need to review sorting and slicing as this is part of a hashmap
        ### we needed to sort in order to solve this problem

        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        res = [item[0] for item in sorted_items[:k]]

        return res
'''

## this is the optimized solution 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## PART 1:
        hashmap = {}

        for i in nums:
            ## big difference 
            #3 we're not using nums[i] instead only i,
            ## this must be because we're not getting the range(len()) 
            ## of nums!!
            hashmap[i] = 1 + hashmap.get(i, 0) 

        ## PART 2:

        bucket = [[] for i in range(len(nums) + 1)]

        for i, frequency in hashmap.items():
            bucket[frequency].append(i)
        
        result = []


        ### PART 3:
        for i in range(len(bucket) -1, 0, -1):
            for number in bucket[i]:
                result.append(number)
                if len(result) == k:
                    return result