import random
import os
def tambah(a):
    for i in range(12):
        input('ketuk enter untuk tambah angka acak')
        os.system('cls')
        a.append(random.randint(1,100))
        print(a)
        if len(a) == 12:
            print('angka akan di sort')
            return mergeSort(a)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        mergeSort(l)
        mergeSort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
  
def printList(arr):
    print(arr)
  
  
arr = []
tambah(arr)
mergeSort(arr)
print("setelah diurutkan: ")
printList(arr)