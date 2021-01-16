# 1 2 3 4 5 -> [1, 2, 3, 4, 5]
a = list(map(int, input().split()))
#########################
# запись и чтение файла #
#########################
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
########################
# игры с чтением файла #
########################
f = open('qq.txt', 'r', -1, 'utf-8')
f_5 = f.read(3)
f.close()

print(f_5)

f = open('qq.txt', 'r', -1, 'utf-8')
f_all = f.read()
f.close()

print(f_all)
print('---------')

f = open('qq.txt', 'r', -1, 'utf-8')
for line in f:
    print(line, end='')
f.close()

f = open('qq.txt', 'w', -1, 'utf-8')
f.write("А тебе пока")
f.close()

f = open('qq.txt', 'r', -1, 'utf-8')
f_all = f.read()
f.close()
print("")
print(f_all)
##############################
# заполнение массива змейкой #
##############################
n = int(input())
m = int(input())
for j in range(n):
    print(' '.join([str(i + 1 + m * j) for i in range(m)][::pow(-1, j)]))
##############################
#    нормальное округление   #
##############################
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)