def find_on_row(way, array, way_index, row_index):
    if way_index == len(way):  # found answer
        return []
    for col_index in range(len(array[0])):
        if array[row_index][col_index] == way[way_index]:
            candidate_answer = find_on_col(way, array, way_index + 1, col_index)
            if not candidate_answer is None:  # unwind answer
                return [col_index+1] + candidate_answer
    return None


def find_on_col(way, array, way_index, col_index):
    if way_index == len(way):  # found answer
        return []
    for row_index in range(len(array)):
        if array[row_index][col_index] == way[way_index]:
            candidate_answer = find_on_row(way, array, way_index + 1, row_index)
            if not candidate_answer is None:  # unwind answer
                return [row_index+1] + candidate_answer
    return None


way = []
waylen = int(input())
wayin = list(map(str, input().split()))
for i in range(waylen):
    way.append(wayin[i])
k = int(input())
array = [[0 for j in range(k)] for i in range(k)]

for i in range(k):
    a = list(map(str, input().split()))
    for j in range(k):
        array[i][j] = a[j]

print(f'{find_on_row(way, array, 0, 0)}')

