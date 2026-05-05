class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        days = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append(i)
            elif temperatures[stack[-1]] >= t:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < t:
                    days[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        
        return days