class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                second_op = stack.pop()
                first_op = stack.pop()
                stack.append(first_op + second_op)
            elif t == '-':
                second_op = stack.pop()
                first_op = stack.pop()
                stack.append(first_op - second_op)
            elif t == '*':
                second_op = stack.pop()
                first_op = stack.pop()
                stack.append(first_op * second_op)
            elif t == '/':
                second_op = stack.pop()
                first_op = stack.pop()
                stack.append(int(first_op / second_op))
            else:
                stack.append(int(t))
        
        return stack[-1]