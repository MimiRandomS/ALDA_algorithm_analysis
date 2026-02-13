
def quick_sort(arr):
    n = len(arr)                                            # O(1): Assignation
    if n <= 1: return arr                                   # O(1): Assignation and return

    pivot = arr[0]                                          # O(1): Assignation
    left, right = [], []                                    # O(1): Assignation

    for i in range(1, n):                                   # O(n): loop in list
        if arr[i] < pivot: left.append(arr[i])              # O(1): Comparison
        elif arr[i] > pivot: right.append(arr[i])           # O(1): Comparison

    return quick_sort(left) + [pivot] + quick_sort(right)   # O(n): concatenation
                                                            # Θ: T(n) = 2T(n/2) + O(n)
                                                            # T(n) = Θ(n log n) average
                                                            # T(n) = T(n−1) + O(n)
                                                            # worst case: pivot is min or max O(n^2)

