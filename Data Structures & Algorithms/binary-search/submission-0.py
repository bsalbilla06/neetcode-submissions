class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            i = (r-l) // 2 + l
            if target == nums[i]:
                return i
            if target < nums[i]:
                r = i-1
            else:
                l = i+1
        return -1