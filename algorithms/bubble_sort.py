
def bubble_sort(arr):
    n = len(arr)                                        # O(1) Assignation
    for i in range(n):                                  # O(n) loop for in list
        for j in range(0, n - 1 - i):                   # O(n^2) because (n−1)+(n−2)+(n−3)+⋯+1 = ∑[n(n - 1)/2] loop in loop in list
            if arr[j] > arr[j + 1]:                     # O(1) comparison
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # O(1) swap
                                                        # O(n):
                                                        # = O(1) + O(1) + O(1) + O(n) + O(n^2)
                                                        # = O(n^2)
                                                        # dominant term
