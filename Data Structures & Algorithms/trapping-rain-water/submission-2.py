class Solution:
    def trap(self, height: List[int]) -> int:
        # left_max = [0]*len(height)
        # for i in range(len(height)):
        #     if i == 0:
        #         left_max[i] = height[i]
        #         continue
        #     left_max[i] = max(left_max[i-1], height[i])

        # right_max = [0]*len(height)
        # for j in range(len(height)-1,-1,-1):
        #     if j == len(height)-1:
        #         right_max[j] = height[j]
        #         continue
        #     right_max[j] = max(height[j], right_max[j+1])

        # max_vol = 0
        # for k in range(len(height)):
        #     max_vol+=((min(left_max[k],right_max[k]))-height[k])

        # return max_vol

        left, right = 0, len(height)-1
        left_max, right_max = 0,0
        max_vol = 0
        while left<right:
            if height[left]<=height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    max_vol+=left_max-height[left]
                left+=1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    max_vol+=right_max-height[right]
                right-=1
        return max_vol