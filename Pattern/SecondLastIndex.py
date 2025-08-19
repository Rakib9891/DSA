# Problem: Return The Second Highest element of an Array

# You are given a numbers array. You have to return the previous value of highest value index 


# Example 1:

#     Input: nums = [33,23,40,35,65,66,76,54,86,64,80,]
#     Output: 80
#     Explanaton: 86 is the highest value and 80 is the closest value of 86.

# Constraint
#   1 < nums.lenght <= 10^6


class Solution:
    def seconHighestIndex(self, nums):
        res = 0
        highest_value = 0
        
        for i in range(len(nums)):
            if highest_value < nums[i]:
                highest_value = nums[i]
            if res < highest_value:
                if nums[i] < highest_value and res < nums[i]:
                    res = nums[i]
            
        return res
n = [33,23,40,86,35,65,66,76,54,64,80]
n = [0, -1, -2]
solution = Solution().seconHighestIndex(n)
print(solution)
# WRONG !!
