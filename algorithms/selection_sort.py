from random import randint
import time


def main():
    short_list = []
    long_list = []
    for i in range(20):
        short_list.append(randint(0, 99))
    print("Unsorted: ", short_list)
    selection_sort(short_list)
    print("Sorted:   ", short_list)
    for i in range(10000):
        long_list.append(randint(0, 9999))
    print("Sorting list with 10,000 elements:")
    start = time.time()
    selection_sort(long_list)
    print(f"Sorted in {time.time() - start} seconds")


def selection_sort(my_list):
    for i in range(len(my_list)):
        smallest = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[smallest]:
                smallest = j
        my_list[i], my_list[smallest] = my_list[smallest], my_list[i]


main()
