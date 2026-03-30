class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            add = True
            while stack:
                if stack[-1] < 0 and a < 0 or stack[-1] > 0 and a > 0:
                    add = True
                    break
                elif stack[-1] > 0 and a < 0 and abs(stack[-1]) == abs(a):
                    print(stack)
                    add = False
                    stack.pop()
                    break
                elif stack[-1] > a and abs(stack[-1]) < abs(a):
                    add = True
                    stack.pop()
                elif stack[-1] > a and abs(stack[-1]) > abs(a):
                    add = False
                    break
                elif stack[-1] < 0 and a > 0:
                    add = True
                    break
            if add:
                stack.append(a)
        return stack
