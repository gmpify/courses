import pytest

def test_sorted():
    assert my_sort([3,2,1]) == [1,2,3]

def my_sort(input):
    return sorted(input)

pytest.main()
