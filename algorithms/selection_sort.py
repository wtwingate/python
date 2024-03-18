from random import randint


def main():
    my_list = []
    for i in range(20):
        my_list.append(randint(0, 99))
    print("Unsorted: ", my_list)
    print("Sorted:   ", selection_sort(my_list))


def selection_sort(my_list):
    """Sort list using selection sort algorithm"""
    for i in range(len(my_list)):
        smallest = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[smallest]:
                smallest = j
        my_list[i], my_list[smallest] = my_list[smallest], my_list[i]
    return my_list


main()
