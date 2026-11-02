"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            meet1 = intervals[i - 1]
            meet2 = intervals[i]

            if meet1.end > meet2.start:
                return False
        
        return True