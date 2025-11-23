def countsort(a):
    mi=min(a)
    size=max(a)-mi+1
    arr=[0]*size
    for num in a:
        arr[num-mi]+=1
    asort=[]
    for i in range(size):
        while arr[i+mi]>0:
            asort.append(i+mi)
            arr[i+mi]-=1
    return asort

a=list(map(int,input().split()))
