class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        cmax = 0
        for num in s:
            if num-1 not in s:
                cmax = max(cmax, self.count(s, num))
        return cmax
    def count(self, s: set[int], start: int) -> int:
        res = 1
        while start + 1 in s:
            res += 1
            start += 1
        return res