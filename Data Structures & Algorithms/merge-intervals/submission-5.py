class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            cur = i
            while stack and cur[0] <= stack[-1][1]:
                stack0, stack1 = stack.pop()
                cur = [stack0, max(stack1, cur[1])]
            stack.append(cur)
    
        return stack