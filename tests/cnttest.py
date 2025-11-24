from src.sorts.cnt import countsort

def test_countsort_basic():
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert countsort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_countsort_sorted():
    arr = [1, 2, 3, 4, 5]
    assert countsort(arr) == [1, 2, 3, 4, 5]

def test_countsort_reverse():
    arr = [5, 4, 3, 2, 1]
    assert countsort(arr) == [1, 2, 3, 4, 5]

def test_countsort_single():
    arr = [52]
    assert countsort(arr) == [52]

def test_countsort_empty():
    arr = []
    assert countsort(arr) == []

def test_countsort_negative():
    arr = [-5, -1, -3, 0, 2, -4]
    assert countsort(arr) == [-5, -4, -3, -1, 0, 2]

def test_countsort_large_numbers():
    arr = [1000, 500, 1500, 750]
    assert countsort(arr) == [500, 750, 1000, 1500]

def test_countsort_duplicates():
    arr = [7, 7, 7, 7, 7]
    assert countsort(arr) == [7, 7, 7, 7, 7]

def test_countsort_wide_range():
    arr = [1, 100, 50, 25, 75]
    assert countsort(arr) == [1, 25, 50, 75, 100]

def test_countsort_mixed():
    arr = [5, -2, 3, 0, 1]
    assert countsort(arr) == [-2, 0, 1, 3, 5]