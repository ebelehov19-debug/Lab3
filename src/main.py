from src.sorts.buble import bublesort
from src.sorts.cnt import countsort
from src.sorts.radix import radixsort
from src.sorts.qsort import qsort
from src.fibandfact.fact import fact
from src.fibandfact.factr import factr
from src.fibandfact.fib import fib
from src.fibandfact.fibrec import fibr
from src.sorts.busket import bucket_sort
def main():
    print("Приветстую!!! Ведите название команды и входные данные. Для полуения подробного списка команд напишите help!")   
    while (a := input()) != 'exit':
        if not len(a):
            continue
        a=a.split()
        if a[0]=="help":
            print("Сначала демонстрируется имя команды потом входные данные потом выходные")
            print("bublesort list[int]->list[int]")
            print("countsort list[int]->list[int]")
            print("radixsort list[int],base: int=10)->list[int] только неотрицательные")
            print("qsort list[int]->list[int]")
            print('bucketsort list[float]->list[float]')
            print('factorial int:n->int')
            print('factorialrec int:n->int')
            print('fib int:n->int')
            print('fibrec int:n->int')
        elif a[0]=='bublesort':
            b=list(map(int,a[1:]))
            print(*bublesort(b))
        elif a[0]=="countsort":
            b=list(map(int,a[1:]))
            print(*countsort(b))
        elif a[0]=='radixsort':
            b=list(map(int,a[1:]))               
            print(*radixsort(b))
        elif a[0]=='qsort':
            print(*qsort(list(map(int,a[1:]))))
        elif a[0]=="fib":
            print(fib(int(a[1])))
        elif a[0]=='fibrec':
            print(fibr(int(a[1])))
        elif a[0]=='factorial':
            print(fact(int(a[1])))
        elif a[0]=="factorialrec":
            print(factr(int(a[1])))
        elif a[0]=='bucketsort':
            b=[float(x) for x in a[1:]]
            print(*bucket_sort(b))
        else:
            print("Неизвестная команла!!! Для списка команд напишите help!")
            
                

        

main()

