d = {'string': 1}

#  'sam' : 2223456, 'edward' : 1234321,

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
    lines = line.split("\t")   # words and lines are the same thing here
    for word in lines:
        words = word.split(' ')  # words and lines are the same thing here
        print("words: ", words)
        # for item in words:
        #     print(words[item])
    print("lines: ", lines)


    # print("lines[0] ;", lines[0])
    # for row in lines:
    #     listitems = lines.split()
    #     print('listitmes: ', listitems)


my_dict = {"Name":[],"Address":[],"Age":[]};

my_dict["Name"].append("Guru")
my_dict["Address"].append("Mumbai")
my_dict["Age"].append(30)
print(my_dict)
print(my_dict.values())
print(my_dict.keys())
print(my_dict.get("Age"))
print(my_dict.get(30))  # answer is none
print(my_dict.fromkeys('Name'))

x = ('key1', 'key2')
y = 0
print()