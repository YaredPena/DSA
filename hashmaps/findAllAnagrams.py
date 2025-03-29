'''
I needed to search up the solution...

since I couldn't solve it break it down to the CORE idea of how this solves that problem

then try to optimize it to do only 1 pass

'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_map = {}
        s_map = {}
        res = []

        for i in range(len(p)):
            p_map[p[i]] = 1 + p_map.get(p[i], 0)
            s_map[s[i]] = 1 + s_map.get(s[i], 0)

        if s_map == p_map:
            res.append(0)

        l = 0

        for r in range(len(p), len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            s_map[s[l]] -= 1

            if s_map[s[l]] == 0:
                s_map.pop(s[l])
            
            l += 1 

            if s_map == p_map:
                res.append(l)
        return res


solution = Solution()
print(solution.findAnagrams("abacbabc", "abc"))


'''review this problem'''