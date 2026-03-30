"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        print([(x.start, x.end) for x in intervals])
        stack = []
        for i in intervals: 
            cur_start, cur_end = i.start, i.end
            if not stack:
                stack.append(i)
            elif stack and (stack[-1]).end <= cur_start:
                stack.append(i)
            else:
                return False
        
        return True