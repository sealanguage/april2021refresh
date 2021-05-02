# Enter your code here. Read input from STDIN. Print output to STDOUT

s = int(input())
word = input()
rank = input()

# print(s, word, rank)  # prints 2 Hacker Rank

# number_string = "1020304050"
# print(number_string[0:-1:2])

print(word[0:7:2], word[1:7:2])
print(rank[0:4:2], rank[1:4:2])
