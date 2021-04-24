if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

        inList = name, score
        print(inList)

        # sorted_inList = sorted(inList)

        # inList.sort(key = lambda x : x[1])

        # Output = sorted(inList[0][0], key = float)

        # print(sorted_inList)
        # print(name, score)
        # print(score)

        # this list with int and floats sorts correctly
        # L = [15, 22.4, 8, 10, 3.14]
        # sorted_list = sorted(L)
        # print(sorted_list)