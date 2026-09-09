"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = [s.start for s in intervals]
        start_times = sorted(start_times, key = lambda x:x)
        end_times = [e.end for e in intervals]
        end_times = sorted(end_times, key = lambda x:x)

        count = 0

        s,e = 0,0
        while s<len(intervals):
            if start_times[s]<end_times[e]:
                count+=1
                s+=1
            else:
                s+=1
                e+=1
        return count
