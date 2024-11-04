"""
3163. String Compression III

Example 1:
Input: word = "abcde"
Output: "1a1b1c1d1e"

Example 2:
Input: word = "aaaaaaaaaaaaaabb"
Output: "9a5a2b"

Example 3:
Input: word = "aaaaaaaaay"
Output: "9a1y"
"""

# =========== SOLUTION =========== #

class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 0:
            return word

        comp = ''
        counter = 0
        current = None

        for letter in word:
            if current is None:
                current = letter
                counter = 1
                continue

            if letter != current:
                comp += f"{counter}{current}"
                current = letter
                counter = 1
                continue

            counter += 1
            if counter == 9:
                comp += f"{counter}{current}"
                current = None
                counter = 0

        return comp if not counter else comp + f"{counter}{current}"

# =========== TEST =========== #

solution = Solution()
print(solution.compressedString('aaaaaaaaay'))