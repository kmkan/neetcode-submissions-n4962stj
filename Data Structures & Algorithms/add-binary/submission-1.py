class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = 0
        num_b = 0
        for i in range(len(a)):
            num_a = num_a + int(a[len(a) - i - 1]) * 2 ** i
        
        for i in range(len(b)):
            num_b = num_b + int(b[len(b) - i - 1]) * 2 ** i
        
        print(num_a, num_b, num_a + num_b)
        total = num_a + num_b

        if total == 0:
            return "0"

        ans = []

        while total > 0:
            ans.append(str(total & 1))
            total >>= 1
        
        return ''.join(ans[::-1])