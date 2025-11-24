from src.sorts.buble import bublesort
def test_bubblesort_basic():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bublesort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_bubblesort_sorted():
    arr = [1, 2, 3, 4, 5]
    assert bublesort(arr) == [1, 2, 3, 4, 5]

def test_bubblesort_reverse():
    arr = [5, 4, 3, 2, 1]
    assert bublesort(arr) == [1, 2, 3, 4, 5]

def test_bubblesort_duplicates():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert bublesort(arr) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_bubblesort_single():
    arr = [42]
    assert bublesort(arr) == [42]

def test_bubblesort_empty():
    arr = []
    assert bublesort(arr) == []

def test_bubblesort_negative():
    arr = [-5, -1, -3, 0, 2, -4]
    assert bublesort(arr) == [-5, -4, -3, -1, 0, 2]

def test_bubblesort_same_elements():
    arr = [7, 7, 7, 7]
    assert bublesort(arr) == [7, 7, 7, 7]

