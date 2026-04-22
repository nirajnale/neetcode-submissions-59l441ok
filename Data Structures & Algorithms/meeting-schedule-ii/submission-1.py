"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        # FIX HERE
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = e = 0
        rooms = 0
        maxRooms = 0

        while s < len(intervals):
            if start[s] < end[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1

            maxRooms = max(maxRooms, rooms)

        return maxRooms