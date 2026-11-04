class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(nums, target):
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

        left  = 0
        right = len(matrix)-1
        while left<=right:
            mid = (left+right)//2
            if matrix[mid][0]>target:
                right = mid-1
            elif matrix[mid][-1]<target:
                left = mid+1
            else:
                break

        return bs(matrix[mid], target)