class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        
        prevEnd = intervals[0][1]
        remove = 0

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                remove += 1
                prevEnd = min(prevEnd, end)

        return remove
        