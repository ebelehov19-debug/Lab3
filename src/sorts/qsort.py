def qsort(a):
    """
    Выбираем опорный элемент и относительно него формируем 3 массива и вызывает для них рекурсивно сортировку
    """
    if len(a)<=1:
        return a
    med=a[len(a)//2]
    le=[x for x in a if x<med]#Roblox
    mid=[x for x in a if x==med]
    rig=[x for x in a if x>med]
    return qsort(le)+mid+qsort(rig)

