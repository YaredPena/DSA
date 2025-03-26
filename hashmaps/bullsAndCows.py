## this problem reminded me heavily of valid anagram

''' 
This was my original solution I believe this called a two pass approach since I'm using two loops
it's O(n) no nesting 

the idea was in the first pass I was going to only get the values into both of my hashmaps 
THEN
in the second pass I was going to do two checks: (after iterating over s_map)
if the key was in g_map AND the index was in the same position for s_map and g_map 
--> increment x by 1 (my bull)

otherwise, if the key was in g_map but the index was NOT in the same position in s_map
--> increment y by 1 (my cow)

class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        x = 0 
        y = 0

        s_map = {}
        g_map = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
            else: 
                s_map[secret[i]] = s_map.get(secret[i], 0)
                g_map[guess[i]] = g_map.get(guess[i], 0) 
        
        for key in s_map:
            if key in g_map and s_map[key] == g_map[key]:
                x += 1
            elif key in g_map and s_map[key] is not g_map[key]:
                y += 1 
        return f"{x}A{y}B"

        Where did I mess up?
        so I had the right idea but I wasn't checking for the frequency of the values!!

            s_map[secret[i]] = s_map.get(secret[i], 0)
            g_map[guess[i]] = g_map.get(guess[i], 0) 
            
            this is NOT INCREASING the values inside of my hashmaps
            basically it's getting all of my values but setting them to zero...

        I was trying to add to bulls through my hashmaps by iterating over the s_map but because I wasn't tracking frequency 
        my values were never going to add properly.

        if key in g_map and s_map[key] == g_map[key]:
                x += 1
        basically all values in both hashmaps are at zero and when a value is encountered it's increment by 1
        
        I had the right idea but this no where near the right way to implement this:
        this is checking for if the key between the two hashmaps are NOT the same INSTANCE
        their not comparing values

        elif key in g_map and s_map[key] is not g_map[key]:
                y += 1 

                This was as I was fixing my problem
                ### x += 1 <-- this was my base case, there is nothing to do but increment x in this situation!!!!!!!!!!!
                ##y += 1 <-- it's not enough to just count like this because what if we have duplicates of the same value 
                ## just at different keys
                ## stole this line from chat gpt I was VERY confused because I looking at
                ## how I was counting in my first pass not here.



        The Proper Approach:
        just incremented x if the positions for secret and guess for a value were the same 
        (this was a base case I should've seen that sooner)

        Then I could've
        gotten all the values into the hashmaps AND counted their frequencies (VALID ANAGRAMS)

        from there all I had to do was just check if a key in my secret hashmap was actually in my 
        guess hashmap
'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        x = 0 
        y = 0

        s_map = {}
        g_map = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
            else:
                s_map[secret[i]] = s_map.get(secret[i], 0) + 1
                g_map[guess[i]] = g_map.get(guess[i], 0) + 1
               
        for key in s_map:
            if key in g_map:
                y += min(s_map[key], g_map[key])

        return f"{x}A{y}B"

solution = Solution()

print(solution.getHint("1122","2211"))