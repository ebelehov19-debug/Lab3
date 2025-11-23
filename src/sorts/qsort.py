def qsort(a):
    if len(a)<=1:
        return a
    med=a[len(a)//2]
    le=[x for x in a if x<med]#Roblox
    mid=[x for x in a if x==med]
    rig=[x for x in a if x>med]
    return qsort(le)+mid+qsort(rig)
a=list(map(int,input().split()))
print(qsort(a))
