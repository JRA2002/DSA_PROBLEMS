'''You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.'''

def right_interval(intervals: list):
    pass

intervals = [[3,4],[2,3],[1,2]]

print(right_interval(intervals))