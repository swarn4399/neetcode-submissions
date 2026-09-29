class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            temp = [dp[k] for k in range(i) if nums[k]<nums[i]]
            dp[i] = 1 + max(temp, default = 0)
        
        return max(dp)