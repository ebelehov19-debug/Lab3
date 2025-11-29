def radixsort(a:list[int],base: int=10)->list[int]:
    """
    создаем несколько корзин и начинаем сортировать числа по последнему разряду 
    """
    if not a:
        return a
    mx=max(a)
    mxl=len(str(mx))

    for i in range(mxl):
        b=[[] for _ in range(base)]
        for num in a:
            rasr=num//(base**i)%10
            b[rasr].append(num)
        a=[]
        for i in b:
            a.extend(i)
    return a


