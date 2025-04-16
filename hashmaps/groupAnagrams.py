'''
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Example 1:

                 0.    1.     2.     3.
Input: strs = ["act","pots","tops","cat","stop","hat"]

act = 0 

pots = 1

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        '''

        ## understand:
        ## strs = ["act","pots","tops","cat","stop","hat"]

        ##  Goal : group all anagrams together into sublists. 
        ##          You may return the output in any order.

        ## base cases: 
        ##
        ## strs = []??
        ##      return []

        ## strs = ['x']??
        ##      return strs

        ## res = [] the idea store result array inside of strs array
        ## for multi array output.


        ##

        ## plan: 
        ## strsCount = {}
        ## key = char : value = i

        ## iterate over strs
        ##  for s in range(len(strs)):
        ## 
        ##       get the frequency of each character within a string in strs
        ##      strs[s[i]] = 1 + strsCount.get(s[i], 0)
        ##   
        ## if a string is equal to another string:
        ##      res.append(s)
        ##
        ## otherwise: 
        ## 

'''
    def result(self, res List[str]) -> List[List[str]]: 
        store all strings

        format all strings [], [], []

        ## putting strs, strings in result array
        ## for s in strs:
        ##  res.append(s)
        ##      return strs[res] ==> [['x']]
        
    for s in strs:
        inner_list = []
        for s in result:
            inner_list.append(s)
        list_of_lists_2.append(inner_list)
    '''