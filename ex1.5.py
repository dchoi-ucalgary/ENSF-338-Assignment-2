import timeit
import matplotlib.pyplot as plt

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    cache = {}

    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
            return cache[n]

old_list = []
new_list = []
n_list = []

for i in range(1,35):
    n_list.append(i)

for i in range(1,35):
    elapsed_time = timeit.timeit(lambda: fib(i), number=1)
    old_list.append(elapsed_time)

for i in range(1,35):
    elapsed_time = timeit.timeit(lambda: fib(2), number=1)
    new_list.append(elapsed_time)

plt.plot(n_list, old_list , 'r' , label='Old Program')
plt.plot(n_list, new_list, 'g', label='New Program')
plt.legend()
plt.xlabel("n")
plt.ylabel("Time")
plt.show()