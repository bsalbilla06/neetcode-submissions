class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hmap = {}
        t_hmap = {}
        for c in s:
            if not c in s_hmap:
                s_hmap[c] = 1
            else:
                s_hmap[c] += 1

        for c in t:
            if not c in t_hmap:
                t_hmap[c] = 1
            else:
                t_hmap[c] += 1

        return s_hmap == t_hmap