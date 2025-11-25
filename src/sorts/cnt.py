def countsort(a:list[int])->list[int]:
    """
    На вход принимает массив интов, а возвращает отсортированный 
    Идея пройтись по исходному массиву  и посчитать количество вхождений всех чисел и восстановить исходный опираясь на массив счетчиков
    """
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

