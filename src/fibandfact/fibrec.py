from functools import*
# def fibr(n: int )->int:#вариант без кеша
#     if n==0: return 0
#     if n==1: return 1
#     return fibr(n-2)+fibr(n-1)
# print(fibr(int(input())))
@lru_cache(10000)
def fibr(n: int )->int:#вариант c кешем огр рекурсией
    if n==0: return 0
    if n==1: return 1
    return fibr(n-2)+fibr(n-1)

