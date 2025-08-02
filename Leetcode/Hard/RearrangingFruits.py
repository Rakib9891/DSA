# 2561. Rearranging Fruits

# You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

# Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
# The cost of the swap is min(basket1[i],basket2[j]).
# Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

# Return the minimum cost to make both the baskets equal or -1 if impossible.

# Example 1:

# Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
# Output: 1
# Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.


from collections import Counter
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter() # we will count manually 
        m = float('inf') # m will be the min val of both baskets
        
        for b1 in basket1: #manually counting in both baskets.
            freq[b1] += 1
            m = min(m, b1)
        for b2 in basket2:
            freq[b2] -= 1
            m = min(m, b2)
        
        total = []
        for key, val in freq.items():
            if val % 2 != 0:
                return -1
            
            total.extend([key] * (abs(val) // 2)) # val is the imbalance cost so we need to take half of val for each basket.
        
        if not total: # both arr are already equel. No need to swap.
            return 0  # that's why the cost will be 0
            
        total.sort()
        cost = 0
        for fruit in total[: len(total) // 2]:
            cost += min(fruit, 2*m)

        return cost