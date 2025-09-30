from loguru import logger
import time
import random

logger.add("log.log")

def my_decor(func):
    def wrapper(*args):
        logger.info("мой декоратор начал работать")
        logger.info(f"входные данные: {args}")
        start = time.time()
        result=func(*args)
        end = time.time() - start
        logger.info(f"выходные данные: {result}")
        logger.success(f"декоратор закончил работу. функция отработала за {round(end,4)}")
        return result
    return wrapper


@my_decor
def bubble(data):
    N = len(data)
    for i in range(0, N - 1):
        for g in range(0, N - 1 - i):
            if data[g] > data[g + 1]:
                data[g], data[g + 1] = data[g + 1], data[g]
    return data

@my_decor
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
    print(c)
    return c


def split_merge(data):
    N = len(data) // 2
    a, b = data[:N], data[N:]
    if len(a) > 1:
        a = split_merge(a)
    if len(b) > 1:
        b = split_merge(b)
    return merge_list(a, b)


# mylist = [33, 61, 7, 2, 94, 562, -4, 0]
mylist = [random.randint(1, 1000) for i in range(1500) ]
sort_mylist = bubble(mylist)
# sort_mylist1 = split_merge(mylist)
# print(sort_mylist1)


