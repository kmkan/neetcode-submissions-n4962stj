class Solution:
    def tribonacci(self, n: int) -> int:
        fibs = {}

        def fib(m):
            if m == 0:
                return 0
            elif m == 1:
                return 1
            elif m == 2:
                return 1
            
            if m in fibs:
                return fibs[m]
            
            fibs[m] = fib(m - 1) + fib(m - 2) + fib(m - 3)
            return fibs[m]
        
        return fib(n)