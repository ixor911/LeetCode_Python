"""
27. Remove Element

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
"""

# =========== SOLUTION =========== #

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        new_nums = []

        for num in nums:
            if num != val:
                new_nums.append(num)

        nums.clear()
        nums.extend(new_nums)

        return len(nums)


# =========== TEST =========== #

solution = Solution()

nums = [0,1,2,2,3,0,4,2]
print(solution.removeElement(nums, 2))
print(nums)
