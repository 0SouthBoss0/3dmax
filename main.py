def split(word):
    return [char for char in word]


arr = []

count = 0

f = open('24_demo.txt', 'r')
fall = f.read()
a = split(fall)

for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        count += 1
        arr.append(count + 1)
    else:
        count = 0

print(max(arr))
