def heapify(arr, i, heap_size):
    left, right, largest = 2 * i + 1, 2 * i + 2, i          # O(1): assignments
    if left < heap_size and arr[left] > arr[largest]:       # O(1): comparison
        largest = left                                      # O(1): assignment
    if right < heap_size and arr[right] > arr[largest]:     # O(1): comparison
        largest = right                                     # O(1): assignment
    if largest != i:                                        # O(1): comparison
        arr[i], arr[largest] = arr[largest], arr[i]         # O(1): swap
                                                            # height of binary heap = log n
        heapify(arr, largest, heap_size)                    # O(log n): recursive call down one branch
                                                            # T(n) = T(n/2) + O(1)
                                                            # Using Master Theorem:
                                                            # a = 1, b = 2, f(n) = O(1)
                                                            # n^(log_b a) = n^0 = 1
                                                            # f(n) = Θ(1)
                                                            # T(n) = Θ(log n)

def build_max_heap(arr):
    n = len(arr)                                            # O(1): Assignation
    for i in range(n // 2 - 1, -1, -1):                     # O(n): loop in middle of arr
        heapify(arr, i, n)                                  # O(log n) per call
                                                            # but most nodes are near leaves
                                                            # total cost = Θ(n)

def heap_sort(arr):
    n = len(arr)                                            # O(1): Assignation
    build_max_heap(arr)                                     # O(n)
    for i in range(n - 1, 0, -1):                           # O(n): loop in list
        arr[0], arr[i] = arr[i], arr[0]                     # O(1): swap
        heapify(arr, 0, i)                                # O(log n): restore heap property
    return arr
                                                            # called n times
                                                            # total = n * log n