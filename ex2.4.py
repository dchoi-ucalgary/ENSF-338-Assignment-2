import sys
import math
import json
import matplotlib.pyplot as plt
import timeit

sys.setrecursionlimit(20000)
def func1(arr, low, high):

    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[math.floor((start + end)/2)]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def func1_old(arr, low, high):
    if low < high:
        pi = func2_old(arr, low, high)
        func1_old(arr, low, pi-1)
        func1_old(arr, pi + 1, high)
def func2_old(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high



with open("ex2.json", "r") as read_file:
    content = json.load(read_file)

new_list = []
old_list = []

for i in range(0, 10):
    low = 0
    high = len(content[i]) - 1
    elapsed_time = timeit.timeit(lambda: func1(content[i], low, high), number=1)
    new_list.append(elapsed_time)

for i in range(0, 10):
    low = 0
    high = len(content[i]) - 1
    elapsed_time = timeit.timeit(lambda: func1_old(content[i], low, high), number=1)
    old_list.append(elapsed_time)

n_list = []

for i in range(0,10):
    n_list.append(i)

plt.plot(n_list, old_list , 'r' , label='Old Program')
plt.plot(n_list, new_list, 'g', label='New Program')
plt.legend()
plt.xlabel("n")
plt.ylabel("Time")
plt.show()
