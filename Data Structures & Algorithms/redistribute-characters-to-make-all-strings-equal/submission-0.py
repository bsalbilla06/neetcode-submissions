class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # get letter frequencies
        freqs = [0] * 26
        for word in words:
            for c in word:
                freqs[ord(c)-ord('a')] += 1

        for freq in freqs:
            if freq % len(words) != 0:
                return False
        return True
