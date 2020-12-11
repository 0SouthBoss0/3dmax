def search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return True
    return False


input1 = list(map(int, input().split()))
n = input1[0]
q = input1[1]
arr = []

input2 = list(map(int, input().split()))
for i in range(q):
    arr.append(int(input()))  # ввод

input2.sort()  # словарь
for i in range(len(arr)):
    if search(input2, arr[i]):
        print("YES")
    else:
        print("NO")
