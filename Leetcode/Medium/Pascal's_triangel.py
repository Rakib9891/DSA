# 118. Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]





class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]]

        for i in range(1, numRows):
            
            prev = res[-1]
            cur = [1]

            for j in range(1, len(prev)):
                cur.append( prev[j-1] + prev[j] )

            cur.append(1)
            res.append(cur)

        return res