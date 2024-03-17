from random import randint
import time


def main():
    short_list = []
    long_list = []
    for i in range(20):
        short_list.append(randint(0, 99))
    print("Unsorted: ", short_list)
    print("Sorted:   ", merge_sort(short_list))
    for i in range(10000):
        long_list.append(randint(0, 9999))
    print("Sorting list with 10,000 elements:")
    start = time.time()
    merge_sort(long_list)
    print(f"Sorted in {time.time() - start} seconds")


def merge_sort(my_list):
    """Sort list using the merge sort algorithm"""
    if len(my_list) < 2:
        return my_list
    left = merge_sort(my_list[: len(my_list) // 2])
    right = merge_sort(my_list[len(my_list) // 2 :])
    return merge(left, right)


def merge(left, right):
    """Merge items from two lists from least to greatest"""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


main()
