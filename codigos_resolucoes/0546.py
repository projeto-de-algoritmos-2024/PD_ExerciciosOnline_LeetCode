from functools import lru_cache
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @lru_cache(None)
        def dfs(left: int, right: int, k: int) -> int:
            if left > right:
                return 0
            
            if left == right:
                return (k + 1) * (k + 1)
            
            max_points = (k + 1) * (k + 1) + dfs(left + 1, right, 0)
            
            for i in range(left + 1, right + 1):
                if boxes[left] == boxes[i]:
                    max_points = max(max_points, dfs(left + 1, i - 1, 0) + dfs(i, right, k + 1))

            return max_points

        return dfs(0, n - 1, 0)

