"""
2425. Bitwise XOR of All Pairings

Example 1:

Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 0
Explanation:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
"""
from typing import List


# =========== SOLUTION =========== #


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        if len(nums1) % 2 != 0:
            for num in nums2:
                ans = ans ^ num

        if len(nums2) % 2 != 0:
            for num in nums1:
                ans = ans ^ num

        return ans




# =========== TEST =========== #

solution = Solution()
print(solution.xorAllNums([1,2], [3,4]))












