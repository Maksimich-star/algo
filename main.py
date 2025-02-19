def bubble(data):
    N = len(data)
    for i in range(0, N - 1):
        for g in range(0, N - 1 - i):
            if data[g] > data[g + 1]:
                data[g], data[g + 1] = data[g + 1], data[g]
    return data


def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)
    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def split_merge(data):
    N = len(data) // 2
    a, b = data[:N], data[N:]
    if len(a) > 1:
        a = split_merge(a)
    if len(b) > 1:
        b = split_merge(b)
    return merge_list(a, b)


mylist = [33, 61, 7, 2, 94, 562, -4, 0]
# sort_mylist = bubble(mylist)
# print(sort_mylist)
sort_mylist1 = split_merge(mylist)
print(sort_mylist1)


