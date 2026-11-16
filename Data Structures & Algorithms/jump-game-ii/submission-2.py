class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        curr_end = 0
        jumpcount = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])

            if i == curr_end:
                jumpcount+=1
                curr_end = farthest
                if farthest >= len(nums)-1:
                    break
        return jumpcount