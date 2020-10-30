print("Введите количество учеников: ")
num = int(input())
index = 0
min = 99999999
arr = []
arr2 = []
arr3 = []

print("Введите данные учеников в формате Фамилия Имя Балл: ")
for i in range(num):
    arr.append(str(input()))

for i in range(num):
    q = arr[i]
    q = q.split()
    arr2.append(q[0])
    arr2.append(q[1])
    arr3.append(int(q[2]))

for i in range(len(arr3)):
    if arr3[i] < min:
        index = i
        min = arr3[i]

for i in range(len(arr2)):
    print("Минимум: ", arr2[index * 2], arr2[(index * 2) + 1])
    exit(0)
