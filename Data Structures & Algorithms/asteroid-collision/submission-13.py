class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack or stack[-1] < 0 and a < 0 or stack[-1] > 0 and a > 0:
                stack.append(a)
            else:
                new_a = a
                while stack and stack[-1] > 0 and a < 0:
                    if abs(stack[-1]) > abs(a):
                        new_a = None
                        break
                    elif abs(stack[-1]) < abs(a):
                        new_a = a
                        stack.pop()
                    else:
                        stack.pop()
                        new_a = None
                        break
                if new_a:
                    stack.append(new_a)
        
        return stack
                