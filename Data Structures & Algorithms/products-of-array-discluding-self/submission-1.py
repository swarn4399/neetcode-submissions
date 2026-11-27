class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        init_right = 1
        arr_left = [left]
        for i in range(1, len(nums)):
            arr_left.append(arr_left[i-1]*nums[i-1])

        for right in range(len(nums)-1,-1,-1):
            arr_left[right] = arr_left[right]*init_right
            init_right*=nums[right]
        return arr_left