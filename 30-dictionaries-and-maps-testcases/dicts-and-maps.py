
d = {}

with open('input00.txt') as f:
    lines = f.readlines()
    print("with lines: ", lines)

    for line in f:
        print('line in f: ', line)
        # key, val = line.split()
        # d[str(key)] = int(val)

# print(d)

for line in open('input00.txt'):
    lines = line.split("\t")
    print(lines)
    # for row in lines:
    #     listitems = lines.split()
    #     print('listitmes: ', listitems)

