"""
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Example 3:
Input: nums = [0,0,0,0,3]
Output: 2, nums = [0,3]
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        current = None
        new_nums = []

        for num in nums:
            if num != current:
                current = num
                new_nums.append(num)

        nums.clear()
        nums.extend(new_nums)

        return len(nums)


solution = Solution()

nums = [0,0,0,0,3]
print(solution.removeDuplicates(nums))
print(nums)
