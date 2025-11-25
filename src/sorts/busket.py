def bublesort(a):
    fl=0
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                fl=1
        if fl==0: break
            

    return a


def bucket_sort(a:list[float])->list[float]:
    """
    принимает массив флотов возвращает отсортированный массив 
    Алгоритм распределяет числа по корзинам, сортирует каждую корзину
    отдельно и объединяет результаты
    """
    n = len(a)
    if n == 0:
        return a
    buckets = [[] for _ in range(n)]
    
    for num in a:
        index = int(n * num)
        if index == n:  
            index = n - 1
        buckets[index].append(num)
    for bucket in buckets:
        bublesort(bucket)
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result

