"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        result = []
        intervals.sort(key=lambda x:x.start)
        for interval in intervals:
            if not result or result[-1][1]<=interval.start:
                result.append([interval.start,interval.end])
            else:
                return False
        return True



