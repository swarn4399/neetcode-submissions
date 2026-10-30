class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = max(nums)
        max_so_far, min_so_far = 1,1

        for n in nums:
            tmp = max_so_far*n
            max_so_far = max(n*max_so_far, n*min_so_far, n)
            min_so_far = min(tmp, n*min_so_far, n)
            global_max =max(global_max, max_so_far)
        
        return global_max
