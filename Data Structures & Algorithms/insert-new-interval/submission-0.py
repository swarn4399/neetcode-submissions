class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = intervals+[newInterval]
        intervals = sorted(intervals)
        stack = []

        for i in range(len(intervals)):
            if i == 0:
                stack.append(intervals[i])
            else:
                if stack[-1][1] >= intervals[i][0]:
                    temp = stack.pop()
                    stack.append([temp[0], max(temp[1], intervals[i][1])])
                else:
                    stack.append(intervals[i])
        return stack
