class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        cur_sum = 0
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                cur_sum -= stack.pop()
                continue
            elif op == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
            if len(stack) > 0:
                cur_sum += stack[-1]
        
        return cur_sum
        