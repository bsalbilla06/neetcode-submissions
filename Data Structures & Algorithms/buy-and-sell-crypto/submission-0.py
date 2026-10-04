class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        nmin, nmax = prices[0], prices[0]
        for n in prices:
            if n < nmin:
                nmin, nmax = n, n
            if n > nmax:
                nmax = n
                max_diff = max(max_diff, nmax - nmin)
        return max_diff