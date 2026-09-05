class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for i,x in enumerate(nums):
            diff = target - x
            if diff in prev_map:
                return [prev_map[diff],i]
            else:
                prev_map[x] = i