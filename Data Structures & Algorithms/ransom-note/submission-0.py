class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)
        rn = defaultdict(int)
        for c in magazine:
            mag[c] += 1
        for c in ransomNote:
            rn[c] += 1

        for idx, (key, val) in enumerate(rn.items()):
            if val > mag[key]:
                return False
        
        return True

