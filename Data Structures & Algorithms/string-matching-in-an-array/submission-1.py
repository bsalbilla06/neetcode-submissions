class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for word in words:
            for w in words:
                if word != w and w in word:
                    res.add(w)
        return list(res)
