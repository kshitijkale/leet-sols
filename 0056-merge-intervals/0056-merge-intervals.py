class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:  # Overlapping
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)  # Remove merged interval
            else:
                i += 1  # Only move forward if no merge
        return intervals
