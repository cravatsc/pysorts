import random
import bubble


def main():
    sort_list = []
    for x in range (0, 20):
        sort_list.append(random.randint(0, 100))
    print(sort_list)
    print("-------")
    bubble.sort(sort_list)
    print(sort_list)


if __name__ == '__main__':
    main()
