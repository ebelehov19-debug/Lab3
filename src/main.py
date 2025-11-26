from src.sorts.buble import bublesort
from src.sorts.cnt import countsort
from src.sorts.radix import radixsort
from src.sorts.qsort import qsort
def main():
    print("Приветстую!!! Ведите название команды и входные данные. Для полуения подробного списка команд напишите help!\n")   
    while (a := input()) != 'exit':
        a=a.split()
        if a[0]=="help":
            print("Сначала демонстрируется имя команды потом входные данные потом выходные")
            print("bublesort list[int]->list[int]")
            print("countsort list[int]->list[int]")
            print("radixsort list[int],base: int=10)->list[int] только неотрицательные")
            print("qsort list[int]->list[int]")
        else:
            if a[0]=='bublesort':
                b=list(map(int,a[1:]))
                print(*bublesort(b))
            if a[0]=="countsort":
                b=list(map(int,a[1:]))
                print(*countsort(b))
            if a[0]=='radixsort':
                b=list(map(int,a[1:]))
                print(*radixsort(b))
            if a[0]=='qsort':
                print(*qsort(list(map(int,a[1:]))))
            
                

        

main()

