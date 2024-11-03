"""
648. Replace Words

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

Example 2:
Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output: "a a a a a a a a bbb baba a"
"""

# =========== SOLUTION =========== #

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        # dictionary.sort(key= lambda x: len(x))
        sentence = sentence.split(' ')

        for i in range(0, len(sentence)):
            for replacement in dictionary:
                if sentence[i].startswith(replacement):
                    sentence[i] = replacement

        return " ".join(sentence)




# =========== TEST =========== #

solution = Solution()
print(solution.replaceWords(
    ["cat","bat","rat"],
    "the cattle was rattled by the battery")
)