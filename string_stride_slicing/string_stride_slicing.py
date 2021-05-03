# Enter your code here. Read input from STDIN. Print output to STDOUT

s = int(input())
word = input()
rank = input()

# print(s, word, rank)  # prints 2 Hacker Rank

print(word[0:len(word):2], word[1:len(word):2])  # splits into Hcr ake
print(rank[0:4:2], rank[1:4:2])  # splits into Ra nk

# now need to iterate through the input and replace the middle number with len()
