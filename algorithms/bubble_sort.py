from random import randint


def main():
    my_list = []
    for i in range(20):
        my_list.append(randint(0, 99))
    print("Unsorted: ", my_list)
    print("Sorted:   ", bubble_sort(my_list))


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
