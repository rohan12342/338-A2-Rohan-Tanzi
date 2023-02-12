import sys
import json
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    cache = []
    cache_append = (low,high)
    cache.append(cache_append)
    while cache:
        low, high = cache.pop()
        if low<high:
            pivot = func2(arr, low, high)
            lower_piviot = pivot - 1
            higher_pivot = pivot + 1
            lower = (low,lower_piviot)
            higher = (high, higher_pivot)
            cache.append(lower)
            cache.append(higher)
    

    

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

time_list=[]
f = open("ex2.json")
data = json.load(f)

timings = list()
Indices = list()

for i in data:
    start = time.time()
    func1(i, 0, len(i)-1)
    end = time.time()
    Indices.append(len(i))
    timings.append(end-start)

plt.plot(Indices, timings)
plt.xlabel("index")
plt.ylabel("Times")
plt.title("Quicksort Array Times")
plt.show()