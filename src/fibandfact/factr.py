def factr(n:int)->int:
    if n==0:return 1
    if n==1:return 1
    return n*factr(n-1)

