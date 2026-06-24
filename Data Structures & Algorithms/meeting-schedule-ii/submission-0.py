"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_rooms, cur_rooms = 0, 0
        array = sorted([(i.start, 1) for i in intervals] + [(i.end, -1) for i in intervals])

        for point in array:
            cur_rooms += point[1]
            max_rooms = max(max_rooms, cur_rooms)

        return max_rooms
            


        