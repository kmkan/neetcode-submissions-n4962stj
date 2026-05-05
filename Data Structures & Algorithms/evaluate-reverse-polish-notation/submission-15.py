class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in {'-', '+', '*', '/'}:
                second_op = stack.pop()
                first_op = stack.pop()
                if t == '+':
                    stack.append(first_op + second_op)
                elif t == '-':
                    stack.append(first_op - second_op)
                elif t == '*':
                    stack.append(first_op * second_op)
                else:
                    stack.append(int(first_op / second_op))
            else:
                stack.append(int(t))
        
        return stack[-1]
