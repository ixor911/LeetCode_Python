"""
2375. Construct Smallest Number From DI String

Example 1:
Input: pattern = "IIIDIDDD"
Output: "123549876"

Example 2:
Input: pattern = "DDD"
Output: "4321"

"""


# =========== SOLUTION =========== #

class Solution:
    def find_variants(self, current: str, pattern: str):
        if len(pattern) == 0:
            return [current]

        r = range(int(current[-1]) + 1, 10) if pattern[0] == 'I' else range(int(current[-1]) - 1, 0, -1)

        possibles = [num for num in r if f"{num}" not in current]

        variants = []
        for pos in possibles:
            for variant in self.find_variants(current + f"{pos}", pattern[1:]):
                variants.append(variant)
            # variants.append(self.find_variants([*current, pos], pattern[1:]))

        return variants





    def smallestNumber(self, pattern: str) -> str:
        for i in range(1, 10):
            variants = self.find_variants(f"{i}", pattern)
            if len(variants) != 0:
                break

        return str(min([int(num) for num in variants]))

# =========== TEST =========== #

solution = Solution()
print(solution.smallestNumber("DDD"))