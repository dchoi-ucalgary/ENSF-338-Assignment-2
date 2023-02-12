import sys
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
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

time_list = []

for i in range(0, 10):
    low = 0
    high = len(content[i]) - 1
    elapsed_time = timeit.timeit(lambda: func1(content[i], low, high), number=5)
    time_list.append(elapsed_time)

n_list = []

for i in range(0,10):
    n_list.append(i)

plt.plot(n_list, time_list)
plt.xlabel("Array Index")
plt.ylabel("Time")
plt.show()




