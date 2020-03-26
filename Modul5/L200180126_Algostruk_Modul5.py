#contoh1
def swap(A,p,q):
    tmp  = A[p]
    A[p] = A[p]
    A[p] = tmp
    
#contoh2
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

#5.1 BubbleSort
L = [10,51,2,18,4,31,13,5,23,64,29]
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
#5.2 SelectionSort
def selestionSort(A):
    n = len(A)
    for i in range (n - 1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
#5.3 InsertionSort
def insertionSort(A):
    n = len(A)
    for i in range (1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai


