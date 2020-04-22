from Latihan import *
from Mahasiswa import*


def convert(arr, obj):
    hasil=[]
    for x in range (len(arr)):
        for i in range (len(arr)):
            if arr[x] == obj[i].NIM:
                hasil.append(obj[i])
    return hasil

def urutkanQuick():
    A = []
    for x in Daftar:
        A.append(x.NIM)
    print("Quick Sort")
    quickSort(A)
    for x in convert(A, Daftar):
        print (x.NIM)
        
def urutkanMerge():
    A = []
    for x in Daftar:
        A.append(x.NIM)
    print("\nMerge Sort")
    mergeSort(A)
    for x in convert(A, Daftar):
        print (x.NIM)

urutkanQuick()
urutkanMerge()