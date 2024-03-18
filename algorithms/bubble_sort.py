from random import randint
import time


def main():
    short_list = []
    long_list = []
    for i in range(20):
        short_list.append(randint(0, 99))
    print("Unsorted: ", short_list)
    print("Sorted:   ", bubble_sort(short_list))
    for i in range(10000):
        long_list.append(randint(0, 9999))
    print("Sorting list with 10,000 elements:")
    start = time.time()
    bubble_sort(long_list)
    print(f"Sorted in {time.time() - start} seconds")


def bubble_sort(my_list):
    """Sort list using the bubble sort algorithm"""
    end = len(my_list)
    sorting = True
    while sorting:
        sorting = False
        for i in range(1, end):
            if my_list[i - 1] > my_list[i]:
                sorting = True
                tmp = my_list[i - 1]
                my_list[i - 1] = my_list[i]
                my_list[i] = tmp
    return my_list


main()
