print("Введите количество учеников: ")
num = int(input())

status = 0
arr = []
arr2 = []
arr3 = []
arrotvet = []

# Заполнение массива с клавиатуры
print("Введите данные учеников в формате Фамилия Имя: ")
for i in range(num):
    arr.append(str(input()))

# деление по каждому слову ("Иванов Иван" -> "Иванов", "Иван")
for i in range(num):
    q = arr[i]
    q = q.split()
    arr2.append(q[0])
    arr2.append(q[1])

# удаление имен ("Иванов", "Иван" -> "Иванов")
for i in range(len(arr2)):
    if i % 2 == 0:
        arr3.append(arr2[i])

# проверка на одинаковые фамилии
for i in range(len(arr3)):
    for j in range(len(arr3)):
        if i != j:
            if arr3[i] == arr3[j]:
                status = 1
                arrotvet.append(arr3[i])

if status == 0:
    print("Однофамильцев нет")
else:
    print("Совпадающие фамилии:")
    arrotvet = list(set(arrotvet))

for i in range(len(arrotvet)):
    print(arrotvet[i])
