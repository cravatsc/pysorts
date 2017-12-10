def bubble(list):
    for list_size in range(len(list) - 1, 0, -1):
        for pos in range(list_size):
            if list[pos] > list[pos + 1]:
                swap(list, pos, pos + 1)


def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
