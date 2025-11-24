from src.sorts.busket import bucket_sort
def test_bucket_sort_basic():
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21]
    expected = sorted(arr)
    assert bucket_sort(arr) == expected

def test_bucket_sort_empty():
    arr = []
    assert bucket_sort(arr) == []

def test_bucket_sort_single():
    arr = [0.5]
    assert bucket_sort(arr) == [0.5]

def test_bucket_sort_already_sorted():
    arr = [0.1, 0.2, 0.3, 0.4, 0.5]
    assert bucket_sort(arr) == arr

def test_bucket_sort_reverse():
    arr = [0.5, 0.4, 0.3, 0.2, 0.1]
    expected = sorted(arr)
    assert bucket_sort(arr) == expected

def test_bucket_sort_duplicates():
    arr = [0.3, 0.1, 0.3, 0.2, 0.1, 0.2]
    expected = sorted(arr)
    assert bucket_sort(arr) == expected

def test_bucket_sort_edge_cases():
    arr = [0.0, 0.999, 0.5, 0.001]
    expected = sorted(arr)
    assert bucket_sort(arr) == expected

def test_bucket_sort_same_elements():
    arr = [0.7, 0.7, 0.7, 0.7]
    assert bucket_sort(arr) == arr

def test_bucket_sort_all_zeros():
    arr = [0.0, 0.0, 0.0, 0.0]
    assert bucket_sort(arr) == arr

def test_bucket_sort_near_one():
    arr = [0.99, 0.999, 0.9999, 0.9]
    expected = sorted(arr)
    assert bucket_sort(arr) == expected

def test_bucket_sort_small_numbers():
    arr = [0.001, 0.002, 0.003, 0.0001]
    expected = sorted(arr)
    assert bucket_sort(arr) == expected
