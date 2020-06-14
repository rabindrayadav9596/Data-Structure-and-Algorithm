def even_odd(A):
    left_ptr = 0
    right_ptr = len(A)-1
    while left_ptr < right_ptr:
        if A[left_ptr] % 2 == 0:
            left_ptr += 1
        else:
            A[right_ptr], A[left_ptr] = A[left_ptr], A[right_ptr]
            right_ptr -= 1
    return A


print(even_odd([2, 3, 4, 5, 6]))
