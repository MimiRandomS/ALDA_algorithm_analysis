
def merge(left, right):
    result = []                             # O(1): assignation
    i = j = 0                               # O(1): assignation

    while i < len(left) and j < len(right): # O(n): len(right) + len(left) = n
        if left[i] <= right[j]:             # O(1): comparison
            result.append(left[i])          # O(1): append
            i += 1                          # O(1): addition
        else:
            result.append(right[j])         # O(1): append
            j += 1                          # O(1): addition

    result.extend(left[i:])                 # O(k): extend
    result.extend(right[j:])                # O(k): extend

    return result

def merge_sort(arr):
    if len(arr) <= 1: return arr            # O(1): return and assignation

    middle = len(arr) // 2                  # O(1): assignation
    left = merge_sort(arr[:middle])         # O(n): split
    right = merge_sort(arr[middle:])        # O(n): split

    return merge(left, right)               # O(n)
                                            # Θ: T(n) = 2T(n/2) + O(n)
                                            # T(n) = Θ(n log n)