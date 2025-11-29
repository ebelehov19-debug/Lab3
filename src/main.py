from src.sorts.buble import bublesort
from src.sorts.cnt import countsort
from src.sorts.radix import radixsort
from src.sorts.qsort import qsort
from src.fibandfact.fact import fact
from src.fibandfact.factr import factr
from src.fibandfact.fib import fib
from src.fibandfact.fibrec import fibr
from src.sorts.busket import bucket_sort
from src.sorts.heap import heapSort
from src.stack.stinlist import Stack
def main():
    st = Stack()
    print("Приветствую!!! Введите название команды и входные данные. Для получения подробного списка команд напишите help!")   
    
    while (a := input()) != 'exit':
        try:
            if not len(a):
                continue
            a = a.split()
            
            if a[0] == "help":
                print("Сначала демонстрируется имя команды потом входные данные потом выходные")
                print("bublesort list[int]->list[int]")
                print("heapsort(arr:list[int])")
                print("countsort list[int]->list[int]")
                print("radixsort list[int],base: int=10)->list[int] только неотрицательные")
                print("qsort list[int]->list[int]")
                print('bucketsort list[float]->list[float]')
                print('factorial int:n->int')
                print('factorialrec int:n->int')
                print('fib int:n->int')
                print('fibrec int:n->int')
                print("Список команд для работы со стеком:")
                print("push value - добавить элемент в стек")
                print("pop - удалить и вернуть верхний элемент")
                print("peek - посмотреть верхний элемент без удаления")
                print("len - получить размер стека")
                print("is_empty - проверить пуст ли стек")
                
            elif a[0] == 'bublesort':
                b = list(map(int, a[1:]))
                print(*bublesort(b))
                
            elif a[0] == "countsort":
                b = list(map(int, a[1:]))
                print(*countsort(b))
                
            elif a[0] == 'radixsort':
                t = input("Введите основание системы счисления: ") 
                b = [int(i, int(t)) for i in a[1:]]              
                print(*radixsort(b))
                
            elif a[0] == 'qsort':
                b = list(map(int, a[1:]))
                print(*qsort(b))
                
            elif a[0] == "fib":
                print(fib(int(a[1])))
                
            elif a[0] == 'fibrec':
                print(fibr(int(a[1])))
                
            elif a[0] == 'factorial':
                print(fact(int(a[1])))     
            elif a[0] == "factorialrec":
                print(factr(int(a[1])))     
            elif a[0] == 'bucketsort':
                b = [float(x) for x in a[1:]]
                print(*bucket_sort(b))
            elif a[0] == 'heapsort':
                b=[int(x) for x in a[1:]]
                heapSort(b)
                print(*b)           
            elif a[0] == 'pop':
                try:
                    print(st.pop())
                except Exception as e:
                    print(str(e))
                    
            elif a[0] == 'push':
                if len(a) < 2:
                    print("Ошибка: для команды push требуется значение")
                else:
                    st.push(a[1])
                    print(f'Значение {a[1]} помещено в стек')
            elif a[0] == 'is_empty':
                print(st.is_empty())
                
            elif a[0] == 'peek':
                try:
                    print(st.peek())
                except Exception as e:
                    print(str(e))
                    
            elif a[0] == 'len':
                print(len(st))
                
            else:
                print("Неизвестная команда!!! Для списка команд напишите help!")
                
        except ValueError as e:
            print(f"Ошибка преобразования данных: {e}")
        except IndexError as e:
            print(f"Ошибка: недостаточно аргументов для команды: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

if __name__==main():
    main()