# 961. N-Repeated Element in Size 2N Array
# Pegeonhole Principle
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2):
            if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]:
                return nums[i]
        return nums[-1]
    
    