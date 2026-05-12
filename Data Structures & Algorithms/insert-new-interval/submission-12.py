class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        i = 0
        while i < len(intervals):
            if newInterval and newInterval[0] < intervals[i][0]:
                cur = newInterval
                newInterval = None
            else:
                cur = intervals[i]
                i += 1

            while stack and cur[0] <= stack[-1][1]:
                stack0, stack1 = stack.pop()
                cur = [stack0, max(cur[1], stack1)]
            
            stack.append(cur)
            print(stack)
        
        if newInterval:
            if not stack:
                return [newInterval]
            elif newInterval[0] <= stack[-1][1]:
                stack0, stack1 = stack.pop()
                stack.append([stack0, max(stack1, newInterval[1])])
            else:
                stack.append(newInterval)

        return stack
            