class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
         
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                lst = [nums[i], nums[l], nums[r]]
                s = sum(lst)
                if s == 0 and lst not in res:
                    res.append(lst)
                if s < 0:
                    l += 1
                else:
                    r -= 1

                if l == i:
                    l += 1
                if r == i:
                    r -= 1

        return res
