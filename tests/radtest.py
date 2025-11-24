from src.sorts.radix import radixsort
def test_radixsort_basic():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert radixsort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_radixsort_sorted():
    arr = [1, 2, 3, 4, 5]
    assert radixsort(arr) == [1, 2, 3, 4, 5]

def test_radixsort_reverse():
    arr = [5, 4, 3, 2, 1]
    assert radixsort(arr) == [1, 2, 3, 4, 5]

def test_radixsort_single():
    arr = [42]
    assert radixsort(arr) == [42]

def test_radixsort_empty():
    arr = []
    assert radixsort(arr) == []

def test_radixsort_same_elements():
    arr = [7, 7, 7, 7]
    assert radixsort(arr) == [7, 7, 7, 7]

def test_radixsort_large_numbers():
    arr = [1000, 500, 1500, 750, 200]
    assert radixsort(arr) == [200, 500, 750, 1000, 1500]

def test_radixsort_different_lengths():
    arr = [1, 100, 10, 1000, 10000]
    assert radixsort(arr) == [1, 10, 100, 1000, 10000]

def test_radixsort_with_zeros():
    arr = [0, 100, 50, 0, 25]
    assert radixsort(arr) == [0, 0, 25, 50, 100]

def test_radixsort_duplicates():
    arr = [123, 456, 123, 789, 456]
    assert radixsort(arr) == [123, 123, 456, 456, 789]


