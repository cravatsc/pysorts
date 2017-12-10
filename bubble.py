import random


def bubble(list):
    for list_size in range(len(list), 0, -1):
        last_num = None
        for pos, val in enumerate(list[:list_size]):
            if val < list[pos - 1]:
                swap(list, pos, pos - 1)


def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp


def main():
    sort_list = []
    for x in range (0, 20):
        sort_list.append(random.randint(0, 100))
    print(sort_list)
    print("-------")
    bubble(sort_list)
    print(sort_list)


if __name__ == '__main__':
    main()
