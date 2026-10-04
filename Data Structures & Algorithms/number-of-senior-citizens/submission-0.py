class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for s in details:
            if int(s[-4:-2]) > 60:
                res += 1
        return res
