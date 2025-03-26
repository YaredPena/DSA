class Solution:
    def digitCount(self, num: str) -> bool:
        dct = {}

        for digit in num:
            digit = int(digit)
            dct[digit] = dct.get(digit, 0) + 1

        for i in range(len(num)):
            expected_count = int(num[i])
            actual_count = dct.get(i, 0)
            
            if expected_count != actual_count:
                return False
        
        return True

        ### UMPIRE

        ## understand: 
        ''' 
        The idea of this problem is that the index number for example:
        num[0]
        should appear the same amount of times as the digit that is at our index
        num[0]
        example:
        num[0] = 1
        our index number '0' must appear only once in our string num

        this is the core idea of the problem.
        '''

        ## match:
        '''
        The data structure I think I should use should be a hashmap.

        why? 

        I want to use the hashmaps {key, value} pair system such that my key
        is the index and my value is the frequency amount that index appears

        key = 0
        value = 1
        { index: 0, value: 1}
        '''

        ## plan:
        '''
            base cases:
            return False
            num = "" (empty string)
            num[x] != num.value

            conditions:
            I should make a hashmap

            check_map = {}

            then iterate through the string nums
            
            ## it's a string so try range(len()) NOT enumerate
            for i in enumerate(nums): 
                ###print(i) <-- this just prints every digit in the string
                if i in check_map:
                    check_map[nums] += 1
                else: 
                    check_map[nums] =  1

            as I iterate through the string I want to check if the index
            appears the same number of times as the value at that index.
                
            return True??
        return False??

            
            as I iterate through the string I want to check if the index
            appears the same number of times as the value at that index.

        '''

        '''
        why was my solution wrong?
        ##if num == "":
        ##    return False

        ##else:
        ##    check_map = {}
        ##    for i in range(len(num)):
        ##        if i in check_map:
        ##           check_map[num] += 1
        ##        else:
        ##            check_map[num] = 1
        ##    return False
        ##return True   
        '''