if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_list = []

    for i in arr:
        my_list.append(i)
        my_list.sort()

    # print(my_list)
    for i in my_list:
        if my_list[-1] == my_list[-2]:
            my_list.remove(my_list[-1])
    # print(my_list)
    print(my_list[-2])
