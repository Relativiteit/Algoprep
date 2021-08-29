# psuedo code of insertion sort
"""
for j = 2 to A.length
    key = A[j]
    # Insert A[j] into the sorted sequence A[1..j-1].
    i = j-1
    while i > 0 and A[i] > key
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key """ 

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1 
        # insert A[j] into the sorted sequence A[1...j-1]
        while i>=0 and key < A[i]:
            A[i+1] = A[i]
            i = i -1 
            A[i+1] = key

if __name__ == '__main__':
    A = [39,12,40,5,8,9]
    insertion_sort(A)
    print(A)

