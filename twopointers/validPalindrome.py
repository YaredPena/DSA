class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:
            ## this is basically checking if we get a symbol ignore it
            while left < right and not self.alpha_numeric(s[left]):
                left +=1
            
             ## same here
            while right > left and not self.alpha_numeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def alpha_numeric(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    #### what if it wansn't only alphanumeric characters?
    ##def symbols(self, c):
        ##return #`~!@$%^&*()
               #{}[]|\?/.><,:;""'