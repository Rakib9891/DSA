# 1221. Split a String in Balanced Strings

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

 

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.




class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanece = 0
        balanced_substring = 0

        for i in s:
            if i == 'L':
                balanece += 1
            else:
                balanece -= 1

            if balanece == 0:
                balanced_substring += 1
        
        return balanced_substring


        # if we find L, increase and if we find R, decrease the balance
        # whenever balanece == 0, we find a balaneced substring 