def bublesort(a):
    fl=0
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                fl=1
            if fl==0: break
            print(*a)

    return a
a=list(map(int,input().split()))
print(bublesort(a))
