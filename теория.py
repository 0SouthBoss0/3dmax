# 1 2 3 4 5 -> [1, 2, 3, 4, 5]
a = list(map(int, input().split()))

# запись и чтение файла
f = open('input.txt', 'r')
w = open('output.txt', 'w')

arr = []
max = 0
for line in f.readlines():
    arr.append(int(line))
for i in range(len(arr)):
    if int(arr[i]) % 11 == 0 and arr[i] > max:
        max = arr[i]
w.write(str(max))
f.close()
w.close()

# заполнение массива змейкой

n = int(input())
m = int(input())
for j in range(n):
    print(' '.join([str(i + 1 + m * j) for i in range(m)][::pow(-1, j)]))




