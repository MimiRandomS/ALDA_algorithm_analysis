def quick_sort(arr):
    n = len(arr)                                            # O(1): assignment
    if n <= 1:                                              # O(1): comparison
        return arr                                          # O(1): return
    pivot = arr[0]                                          # O(1): assignment
    left, equal, right = [], [], []                         # O(1): assignment
    for x in arr:                                           # O(n): iterate through list
        if x < pivot:                                       # O(1): comparison
            left.append(x)                                  # O(1): append
        elif x > pivot:                                     # O(1): comparison
            right.append(x)                                 # O(1): append
        else:
            equal.append(x)                                 # O(1): append
    return quick_sort(left) + equal + quick_sort(right)     # O(n): concatenation
                                                            # partitions cost O(n)
                                                            # recursive calls on subarrays
                                                            # Average case:
                                                            # T(n) = 2T(n/2) + O(n)
                                                            # a = 2, b = 2, f(n) = Θ(n)
                                                            # n^(log_b a) = n
                                                            # T(n) = Θ(n log n)
                                                            #
                                                            # Worst case:
                                                            # T(n) = T(n−1) + O(n)
                                                            # T(n) = Θ(n²)
