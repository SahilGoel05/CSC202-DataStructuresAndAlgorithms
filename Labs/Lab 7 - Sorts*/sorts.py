import random
import time

def selection_sort(alist):
    i = len(alist) - 1
    comps = 0
    while i > 0:
        maxPos = 0
        for j in range(1, i + 1):
            comps += 1
            if alist[j] > alist[maxPos]:
                maxPos = j

        keep = alist[i]
        alist[i] = alist[maxPos]
        alist[maxPos] = keep
        i -= 1

    return comps



def insertion_sort(alist):
    i = 1
    comps = 0
    while i < len(alist):
        cur = alist[i]
        pos = i
        while pos > 0 and alist[pos - 1] > cur:
            comps += 1
            alist[pos] = alist[pos - 1]
            pos -= 1

        comps += 1


        alist[pos] = cur
        i += 1

    return comps

def main():
    print("SS:")

    for num in [1000, 2000, 4000, 8000, 16000, 32000]:
        random.seed(1234)
        randoms = random.sample(range(1000000), num)  # Generate num random numbers from 0 to 999,999
        start_time = time.time()
        comps = selection_sort(randoms)
        stop_time = time.time()
        print("n:", num, "- comps:", comps, "- time:", stop_time - start_time)

    print("IS:")

    for num in [1000, 2000, 4000, 8000, 16000, 32000]:
        random.seed(1234)
        randoms = random.sample(range(1000000), num)  # Generate num random numbers from 0 to 999,999
        start_time = time.time()
        comps = insertion_sort(randoms)
        stop_time = time.time()
        print("n:", num, "- comps:", comps, "- time:", stop_time - start_time)

if __name__ == '__main__': 
    main()

