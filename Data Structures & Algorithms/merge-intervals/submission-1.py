class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for i in intervals:
            if not stack:
                stack.append(i)
                continue
            
            cur_start, cur_end = i
            top_start, top_end = stack[-1][0], stack[-1][1]

            if cur_start <= top_end:
                stack.pop()
                stack.append([top_start, max(cur_end, top_end)])
            else:
                stack.append(i)
        
        return stack