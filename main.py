def isInt(n):
    return int(n) == float(n)


OTVET = []

cout = int(input())

for i in range(cout):

    arr = []

    a = list(map(int, input().split()))

    fin = a[0]
    half = a[1]
    k = a[2]
    arr.append(0)
    for i in range(fin):  # ВСЕ I + 1
        i = i + 1

        if i == 1:
            arr.append(1)
        else:
            q = i / k
            w = i - 1

            if i > half:
                if int(q) >= half and isInt(q):
                    arr.append(arr[int(q)] + arr[w])
                else:
                    arr.append(arr[w])

            if i <= half:
                if isInt(q):
                    arr.append(arr[int(q)] + arr[w])
                else:
                    arr.append(arr[w])

    OTVET.append(max(arr))

for i in range(len(OTVET)):
    print(OTVET[i])
