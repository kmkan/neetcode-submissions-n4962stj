class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.sort(key=lambda x: x[0])

        stack = []
        i = 0
        while i < len(intervals):
            cur_start, cur_end = intervals[i]
            new_start, new_end = newInterval

            if not stack and new_start < cur_start:
                stack.append(newInterval)
                newInterval = (float('inf'), float('inf'))
                print(stack)
                continue
            elif not stack:
                stack.append(intervals[i])
                print(stack)
                i += 1
                continue
            
            print(stack)
            insert = None
            if cur_start <= new_start:
                insert = intervals[i]
                i += 1
            else:
                insert = (new_start, new_end)
                newInterval = (float('inf'), float('inf'))
            
            if insert[0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], insert[1])
            else:
                stack.append(insert)
        
        if newInterval[0] <= stack[-1][1]:
            stack[-1][1] = max(stack[-1][1], newInterval[1])
        elif newInterval[0] != float('inf'):
            stack.append(newInterval)
        
        return stack
