class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums, target):
            left = 0
            right = len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return True
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return False

        top = 0
        bot = len(matrix)-1
        while top<=bot:
            row = (top+bot)//2
            if matrix[row][0]<=target and matrix[row][-1]>=target:
                break
            elif matrix[row][0]>target:
                bot = row-1
            else:
                top = row+1
        if top>bot:
            return False
        return binary_search(matrix[row], target)
