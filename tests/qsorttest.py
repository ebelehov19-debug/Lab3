from src.sorts.qsort import qsort
def test_qsort_basic():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert qsort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_qsort_sorted():
    arr = [1, 2, 3, 4, 5]
    assert qsort(arr) == [1, 2, 3, 4, 5]

def test_qsort_reverse():
    arr = [5, 4, 3, 2, 1]
    assert qsort(arr) == [1, 2, 3, 4, 5]

def test_qsort_duplicates():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert qsort(arr) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_qsort_single():
    arr = [42]
    assert qsort(arr) == [42]

def test_qsort_empty():
    arr = []
    assert qsort(arr) == []

def test_qsort_negative():
    arr = [-5, -1, -3, 0, 2, -4]
    assert qsort(arr) == [-5, -4, -3, -1, 0, 2]

def test_qsort_same_elements():
    arr = [7, 7, 7, 7]
    assert qsort(arr) == [7, 7, 7, 7]
