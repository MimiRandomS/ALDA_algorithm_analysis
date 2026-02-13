import pytest
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort

# Test cases que todos los algoritmos deben pasar
test_cases = [
    ([], []),                           # Empty array
    ([1], [1]),                         # Single element
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), # Already sorted
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), # Reverse sorted
    ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]), # Random with duplicates
    ([42], [42]),                       # Single element
    ([-5, -1, -10, 0, 3], [-10, -5, -1, 0, 3]), # Negative numbers
]

@pytest.mark.parametrize("input_arr,expected", test_cases)
def test_bubble_sort(input_arr, expected):
    result = bubble_sort(input_arr.copy())
    assert result == expected

@pytest.mark.parametrize("input_arr,expected", test_cases)
def test_insertion_sort(input_arr, expected):
    result = insertion_sort(input_arr.copy())
    assert result == expected

@pytest.mark.parametrize("input_arr,expected", test_cases)
def test_merge_sort(input_arr, expected):
    result = merge_sort(input_arr.copy())
    assert result == expected

@pytest.mark.parametrize("input_arr,expected", test_cases)
def test_quick_sort(input_arr, expected):
    result = quick_sort(input_arr.copy())
    assert result == expected

@pytest.mark.parametrize("input_arr,expected", test_cases)
def test_heap_sort(input_arr, expected):
    result = heap_sort(input_arr.copy())
    assert result == expected