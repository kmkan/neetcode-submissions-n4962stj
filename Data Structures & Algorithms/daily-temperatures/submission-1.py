class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []
        temps = temperatures
        for i in range(len(temps)): 
            while stack and temps[i] > temps[stack[-1]]:
                days[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return days
