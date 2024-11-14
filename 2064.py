"""
2064. Minimized Maximum of Products Distributed to Any Store

Example 1:
Input: n = 6, quantities = [11,6]
Output: 3

Example 2:
Input: n = 7, quantities = [15,10,10]
Output: 5

Example 3:
Input: n = 1, quantities = [100000]
Output: 100000

Example 4:
Input: n = 2, quantities = [5,7]
Output: 7
"""

# =========== SOLUTION =========== #
import math
from decimal import Decimal

class Solution:
    def find_best(self, n, best, quantities):
        min = math.inf
        sum = 0

        for quantity in quantities:
            value = quantity / best
            sum += math.ceil(value)
            if 0 < math.modf(value)[1]value % 1 < min:
                min = value % 1

        if sum > n:
            print(best * min)
            return self.find_best(n, math.ceil(best + best * min), quantities)
        else:
            return best


    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        best = math.ceil((sum(quantities) / n))
        best = self.find_best(n, best, quantities)

        return int(best)




# =========== TEST =========== #

solution = Solution()
# print(solution.minimizedMaximum(
#     1000,
# [90881,69718,65737,44998,65913,45207,55066,61458,87671,93911,7999,80865,9079,2272,90290,37529,70983]
# ))

print(solution.minimizedMaximum(
    20,
[5,10,20,5,14,22,29,11,12,28,7,13,30,22]
))