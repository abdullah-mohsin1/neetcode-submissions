class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.lower()
        l = 0
        r = len(x) - 1
        while l <= r:
            while l <= r and x[l].isalnum() == False:
                l += 1
            while l <= r and x[r].isalnum() == False:
                r -= 1
            if l > r:
                break
            if  x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True