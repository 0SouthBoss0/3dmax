n = int(input())

for i in range((2 * n - 1) // 2 + 1):
    print("*" * i)

print("*" * n)

for i in range((2 * n - 1) // 2, 0, -1):
    print("*" * i)
