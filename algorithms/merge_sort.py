from random import randint


def main():
    my_list = []
    for i in range(20):
        my_list.append(randint(0, 99))
    print("Unsorted: ", my_list)
    print("Sorted:   ", merge_sort(my_list))


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
