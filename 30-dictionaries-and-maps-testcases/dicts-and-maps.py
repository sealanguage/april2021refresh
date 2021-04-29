
d = {}

with open('input00.txt') as f:
    lines = f.readlines()
    print("with lines: ", lines)

    for line in f:
        line.split(' ')
        print('line in f: ', line)
        # key, val = line.split()
        # d[str(key)] = int(val)

# print(d)

for line in open('input00.txt'):
    lines = line.split("\t")
    for word in lines:
        words = word.split(' ')
        print("words: ", words)
        for item in words:
            print(words[item])
    print("lines: ", lines)


    # print("lines[0] ;", lines[0])
    # for row in lines:
    #     listitems = lines.split()
    #     print('listitmes: ', listitems)

