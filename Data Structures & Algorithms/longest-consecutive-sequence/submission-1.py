class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_len = 0
        for i in range(len(nums)):
            curr_len = 1
            if nums[i]-1 in set_nums:
                continue
            else:
                temp = nums[i]
                while temp+1 in set_nums:
                    curr_len+=1
                    temp+=1
                max_len = max(max_len, curr_len)
        return max_len
