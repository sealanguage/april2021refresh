if __name__ == '__main__':
    n = int(input())  # this is first number, 5 in first test case
    arr = map(int, input().split())
    alist = []

    for num in arr:
        alist.append(num)
        alist.sort()

    new_list = set(alist)
    new_list.remove(max(new_list))
    print(max(new_list))
