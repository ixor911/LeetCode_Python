"""
796. Rotate String

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

Example 3:
Input: s = "aaaab", goal = "aaaba"
Output: true

Example 4:
Input: s = "aaaaa", goal = "aaaaa"
Output: true

Example 5:
Input: s = "", goal = ""
Output: true

Example 6:
Input: s = "aabbaaa", goal = "aabbaaa"
Output: true

Example 7:
Input: s = "defdefdefabcabc", goal = "defdefabcabcdef"
Output: true

"""
from operator import index


# =========== SOLUTION =========== #

class Solution:
    def find_start(self, sl: list, gl: list) -> tuple[int, int]:
        index_s = 0
        index_g = gl.index(sl[0])

        while index_s > -len(sl) + 1 and sl[index_s - 1] == sl[index_s]:
            index_s -= 1
        while index_g > -len(gl) + 1 and gl[index_g - 1] == gl[index_g]:
            index_g -= 1

        return index_s, index_g

    def find_rotate(self, sl: list, gl: list, index_s: int, index_g: int) -> bool:
        for i in range(len(sl)):
            print(index_s, index_g)
            print(sl[index_s], gl[index_g])
            print()
            if sl[index_s] != gl[index_g]:
                return False

            index_s += 1
            index_g += 1

            if index_g == len(gl):
                index_g = 0

        return True

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif len(s) == 0:
            return True

        sl = list(s)
        gl = list(goal)

        index_s, index_g = self.find_start(sl, gl)
        if index_s == -len(sl) + 1 or index_g == -len(gl) + 1:
            return True

        return self.find_rotate(sl, gl, index_s, index_g)



# =========== TEST =========== #

solution = Solution()
print(solution.rotateString("defdefdefabcabc", "defdefabcabcdef"))


