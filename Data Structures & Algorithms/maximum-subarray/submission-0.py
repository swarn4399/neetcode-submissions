class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        running_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum+num)
            running_sum = max(running_sum, curr_sum)
        
        return running_sum