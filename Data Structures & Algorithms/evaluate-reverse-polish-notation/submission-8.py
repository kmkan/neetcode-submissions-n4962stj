class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': 0, '-': 0, '*': 0, '/': 0}
        stack = []
        for t in tokens:
            if t in operators:
                right = stack.pop()
                left = stack.pop()
                if t == '+':
                    stack.append(left + right)
                elif t == '-':
                    stack.append(left - right)
                elif t == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(t))
            print(stack)
        print(stack)
        return stack[-1]