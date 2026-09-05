class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        left_arr = []
        for i in range(len(nums)):
            left_arr.append(left_prod)
            left_prod*=nums[i]

        right_prod = 1
        for j in range(len(nums)-1, -1, -1):
            left_arr[j]*=right_prod
            right_prod*=nums[j]
        return left_arr