class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        def getBestProject(w, profits, capital):
            maxi = -1
            for i in range(len(capital)):
                if capital[i] <= w:
                    if maxi < 0 or profits[i] > profits[maxi]:
                        maxi = i
            return maxi


        for i in range(k):
            index = getBestProject(w, profits, capital)
            if index < 0:
                break
            w += profits.pop(index)
            capital.pop(index)
        return w
