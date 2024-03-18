from random import randint
import time


def main():
    short_list = []
    long_list = []
    for i in range(20):
        short_list.append(randint(0, 99))
    print("Unsorted: ", short_list)
    print("Sorted:   ", quick_sort(short_list, 0, len(short_list) - 1))
    for i in range(10000):
        long_list.append(randint(0, 9999))
    print("Sorting list with 10,000 elements:")
    start = time.time()
    quick_sort(long_list, 0, len(long_list) - 1)
    print(f"Sorted in {time.time() - start} seconds")


def quick_sort(my_list, low, high):
    """Sort list using quick sort algorithm"""
    if low < high:
        pivot = partition(my_list, low, high)
        quick_sort(my_list, low, pivot - 1)
        quick_sort(my_list, pivot + 1, high)
    return my_list


def partition(my_list, low, high):
    """partition list around the pivot element"""
    pivot = my_list[high]
    i = low
    for j in range(low, high):
        if my_list[j] < pivot:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            i += 1
    my_list[i], my_list[high] = my_list[high], my_list[i]
    return i


main()
