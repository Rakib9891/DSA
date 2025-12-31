# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false



class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(l, r):  # healper func (check)
            while l < r: # after deleting it will check is it palindrome
                if s[l] !=  s[r]:
                    return False
                l += 1
                r -= 1
            return True


        l, r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]: 
                return check(l+1, r) or check(l, r-1)     
                # delete left side or right side letter
                # check only exicute if we have delete a letter
            l += 1
            r -= 1
        return True 
        # otherwise it will be a palindrome