class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            m[target-n] = i

        for i, n in enumerate(nums):
            if n in m and i != m[n]:
                return [i, m[n]]