def fact(n:int)->int:
    fa=1
    for i in range(1,n+1):
        fa*=i
    return fa
print(fact(int(input())))
