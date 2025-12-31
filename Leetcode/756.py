# 756. Pyramid Transition Matrix

from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = {}
        for left, right, top in allowed:
            if (left, right) not in mp:
                mp[(left, right)] = []
            mp[(left, right)].append(top)

        def dfs(cur_lvl, position, next_lvl):
            if len(cur_lvl) == 1: # If reached the top of the triangle
                return True
            if position == len(cur_lvl) - 1: # If finished cur lvl
                return dfs(next_lvl, 0, [])

            left = cur_lvl[position]
            right = cur_lvl[position + 1]

            if (left, right) not in mp:
                return False
            
            for top_block in mp[(left, right)]:
                next_lvl.append(top_block)
                if dfs(cur_lvl, position + 1, next_lvl): # If cur choise give true
                    return True
                next_lvl.pop()

            return False

        return dfs(bottom, 0, [])