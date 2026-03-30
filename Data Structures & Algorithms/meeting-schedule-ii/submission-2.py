import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        heapq.heapify(heap)
        intervals.sort(key=lambda x: x.start)
        i = 0
        for i in range(len(intervals)):
            if not heap:
                heapq.heappush(heap, intervals[i].end)
                continue
            
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
            else:
                heapq.heappush(heap, intervals[i].end)
        
        return len(heap)
            