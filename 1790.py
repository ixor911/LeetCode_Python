"""
1790. Check if One String Swap Can Make Strings Equal

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
"""

from typing import List

# =========== SOLUTION =========== #

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        pairs = []
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                if len(pairs) == 2:
                    return False

                pairs.append((s1[i], s2[i]))

        if len(pairs) == 0:
            return True
        elif len(pairs) == 2:
            return pairs[0][0] == pairs[1][1] and pairs[0][1] == pairs[1][0]
        else:
            return False


# =========== TEST =========== #

solution = Solution()
print(solution.areAlmostEqual(s1 = "kelb", s2 = "kelb"))