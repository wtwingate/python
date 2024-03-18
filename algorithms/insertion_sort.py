from random import randint


def main():
    my_list = []
    for i in range(20):
        my_list.append(randint(0, 99))
    print("Unsorted: ", my_list)
    print("Sorted:   ", insertion_sort(my_list))


def insertion_sort(my_list):
    """Sort list using the insertion sort algorithm"""
    for i in range(len(my_list)):
        j = i
        while j > 0 and my_list[j] < my_list[j - 1]:
            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            j -= 1
    return my_list


main()
