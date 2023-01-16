import os
os.system("cls")

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    tengah = len(arr) // 2
    kiri = arr[:tengah]
    kanan = arr[tengah:]
    kiri = merge_sort(kiri)
    kanan = merge_sort(kanan)
    return merge(kiri, kanan)

def merge(kiri, kanan):
    hasil = []
    while kiri and kanan:
        if kiri[0] < kanan[0]:
            hasil.append(kiri.pop(0))
        else:
          hasil.append(kanan.pop(0))
    if kiri:
      hasil += kiri
    elif kanan:
      hasil += kanan
    return hasil

def jumpSearch(arr, x):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev

    return -1

def sort_nested_dataset(dataset) :
    sorted = []
    nested = {} 
    for i in range(len(dataset)) :
        if type(dataset[i]) == str :
            sorted.append(dataset[i])
        else :
            nested[i] = merge_sort(dataset[i])
    sorted = merge_sort(sorted)
    for i in nested :
        sorted.insert(i, nested[i])

    return sorted

dataset = ['daiva', 'zaki', ['wahyu', 'zaki'], 'shafa', ['zaki', 'aji', 'wahyu'], 'zaki']
datasetsorted = sort_nested_dataset(dataset)
x = 'zaki'

for index in range(len(datasetsorted)) :
    if type(datasetsorted[index]) == list :
        kolom = jumpSearch(datasetsorted[index], x)
        if kolom != -1 :
            print(f'{x} berada di array index ke - {index} kolom {kolom}')
    else :
        if datasetsorted[index] == x :
            print(f'{x} berada di array index ke - {index}')
