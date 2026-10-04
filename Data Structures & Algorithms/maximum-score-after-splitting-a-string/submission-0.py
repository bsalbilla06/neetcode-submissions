class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            score = s[:i].count('0') + s[i:].count('1')
            res = max(res, score)

        return res
        