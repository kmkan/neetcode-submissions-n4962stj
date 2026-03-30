class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for b in s:
            if b in brackets:
                stack.append(brackets[b])
            elif not stack or stack[-1] != b:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0