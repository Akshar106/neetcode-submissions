class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0] * n

        for i in range(n):
            ans = 1
            for j in range(n):
                if j == i:
                    continue
                ans = ans * nums[j]
            
            res[i] = ans
        return res