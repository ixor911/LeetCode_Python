"""
3160. Find the Number of Distinct Colors Among the Balls

Example 1:
Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
Output: [1,2,2,3]

Example 2:
Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
Output: [1,2,2,3,4]
"""
from itertools import count
from typing import List
from collections import Counter

# =========== SOLUTION =========== #

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        counter = []
        for ball, color in queries:
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 1

            if ball in balls:
                if colors[balls[ball]] == 1:
                    del colors[balls[ball]]
                else:
                    colors[balls[ball]] -= 1

            balls[ball] = color

            counter.append(len(colors.keys()))

        return counter




# =========== TEST =========== #



solution = Solution()
print(solution.queryResults(limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]))