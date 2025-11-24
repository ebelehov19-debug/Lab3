def countsort(a):
    if not a:
        return a
    mi=min(a)
    size=max(a)-mi+1
    arr=[0]*size
    for num in a:
        arr[num-mi]+=1
    asort=[]
    for i in range(size):
        while arr[i]>0:
            asort.append(i+mi)
            arr[i]-=1
    return asort

