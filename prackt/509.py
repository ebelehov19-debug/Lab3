class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if n==0: return 0
        if n==1:return 1
        for _ in range(n):
            t=a
            a+=b
            b=t
        return a
