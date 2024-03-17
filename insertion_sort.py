from random import randint
import time


def main():
    short_list = []
    long_list = []
    for i in range(20):
        short_list.append(randint(0, 99))
    print("Unsorted: ", short_list)
    insertion_sort(short_list)
    print("Sorted:   ", short_list)
    for i in range(10000):
        long_list.append(randint(0, 9999))
    print("Sorting list with 10,000 elements:")
    start = time.time()
    insertion_sort(long_list)
    print(f"Sorted in {time.time() - start} seconds")


def insertion_sort(my_list):
    """Sort list using the insertion sort algorithm"""
    for i in range(len(my_list)):
        j = i
        while j > 0 and my_list[j] < my_list[j - 1]:
            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            j -= 1
    return my_list


main()
