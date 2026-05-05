class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for p in s:
            if p in parentheses:
                stack.append(parentheses[p])
            elif len(stack) <= 0 or stack[-1] != p:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0