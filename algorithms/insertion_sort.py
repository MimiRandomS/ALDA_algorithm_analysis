
def insertion_sort(arr):
    n = len(arr)                        # O(1) # Assignation
    for i in range(1 , n):              # O(n) loop for in list
        key = arr[i]                    # O(1) Assignation
        j = i - 1                       # O(1) Assignation
        while j >= 0 and key < arr[j] : # O(n^2) because 1+2+3+⋯+(n−1) = ∑[n(n - 1)/2] loop in loop in list
            arr[j + 1] = arr[j]         # O(1) Assignation
            j -= 1                      # O(1) Subtraction
        arr[j + 1] = key                # O(1) Assignation
                                        # O:
                                        # = O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(n) + O(n^2)
                                        # = O(n^2)
                                        # dominant term
