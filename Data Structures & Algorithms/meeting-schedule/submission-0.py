"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        timeline = [(i.start, 1) for i in intervals] + [(i.end, -1) for i in intervals]
        timeline.sort(key=lambda x: (x[0], x[1]))
        meeting = 0

        for time, diff in timeline:
            meeting += diff
            if meeting > 1:
                return False

        return True
