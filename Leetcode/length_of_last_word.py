# 58. Length of Last Word

# premium lock icon
# Companies
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
#1.
        res = 0
        temp = 0
        
        for i in range(len(s)):
            if s[i].isalpha():
                temp += 1
            else:                  # if there is a space it will update the res
                if temp:
                    res = temp
                temp = 0

            if temp:      # for the last index if there isn't any space it also should update res
                res = temp

        # return res

                # Approach   2. 

        i = len(s)-1

        while i>=0 and s[i] == " ":
            i -= 1

        length = 0
        while i>=0 and s[i] != " ":
            length += 1
            i -= 1
            
        return length