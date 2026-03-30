class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        stack = []
        total_remove = 0
        intervals.sort(key=lambda x: x[1])
        for i in intervals:
            if not stack:
                stack.append(i)
                continue
            
            top_start, top_end = stack[-1]
            cur_start, cur_end = i
            if cur_start < top_end:
                total_remove += 1
            else:
                stack.append(i)
        
        return total_remove
