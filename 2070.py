"""
2070. Most Beautiful Item for Each Query

Example 1:
Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]

Example 2:
Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
Output: [4]

Example 3:
Input: items = [[10,1000]], queries = [5]
Output: [0]
"""



# =========== SOLUTION =========== #

class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        d = {}

        for query in queries:
            d[query] = 0

        for item in items:
            suits = [query for query in queries if query >= item[0]]
            for suit in suits:
                if d.get(suit) < item[1]:
                    d[suit] = item[1]

        return [d[query] for query in queries]



# =========== TEST =========== #

solution = Solution()
print(solution.maximumBeauty(
    [[1,2],[3,2],[2,4],[5,6],[3,5]],
    [1,2,3,4,5,6, 2,2,2]
))