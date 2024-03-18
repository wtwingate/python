from random import randint


def main():
    my_list = []
    for i in range(20):
        my_list.append(randint(0, 99))
    my_target = randint(0, 999)
    print(my_list)
    print(f"Checking for subset with a sum of {my_target}")
    if subset_sum(my_list, my_target):
        print("Found!")
    else:
        print("Not found")


def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    if index < 0 and target != 0:
        return False
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)

    result1 = find_subset_sum(nums, target, index - 1)
    result2 = find_subset_sum(nums, target - nums[index], index - 1)
    return result1 or result2


main()
