'''
Created on 2023/10/13

@author: t21cs063
'''
from random import randint

data = [randint(0, 100) for _ in range(100)]

def quick_sort(data: list) -> list:
    if len(data) <= 1:
        return data
    pivot = data.pop()
    left = quick_sort([i for i in data if i <= pivot])
    right = quick_sort([i for i in data if i > pivot])
    return left + [pivot] + right

data = quick_sort(data)
print(*data)
