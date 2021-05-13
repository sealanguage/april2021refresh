# Enter your code here. Read input from STDIN. Print output to STDOUT

# s = int(input())
# word = input()
# rank = input()

# print(s, word, rank)  # prints 2 Hacker Rank

# print("hard coded: ", word[0:len(word):2], word[1:len(word):2])  # WORKS splits into Hcr ake
# print("hard coded: ", rank[0:4:2], rank[1:4:2])  # WORKS splits into Ra nk

# now need to iterate through the input and replace the middle number with len()

if __name__ == '__main__':
    s = input()
    first_word = input()
    second_word = input()

    print(first_word[0:len(first_word):2], first_word[1:len(first_word):2])
    print(second_word[0:len(second_word):2], second_word[1:len(second_word):2])

# for stringy in input():  # prints o and 1

#         print(stringy)

# for letter in word:
#     letter[0:7:2]
#     print(letter)

# for i in range(n):
#     a, b = input().strip().split(' ')
#     print (a, b)

# hack = list(word)
# print(hack)