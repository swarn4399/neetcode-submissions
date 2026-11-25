class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for num in set_nums:
            if num-1 not in set_nums:
                temp = num
                curr_len = 1

                while temp+1 in set_nums:
                    curr_len+=1
                    temp+=1
                
                longest = max(longest, curr_len)

        return longest
        