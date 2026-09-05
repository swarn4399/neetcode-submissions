class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in dict_nums:
                return [dict_nums[nums[i]], i]
            else:
                dict_nums[diff] = i
