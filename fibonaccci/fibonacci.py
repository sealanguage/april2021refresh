# Challenge 2 - Looping - Fibonacci sequence
#   Method Name: Fib
#   Return Type: int
#   parameters: int pos
# the method should return the number that falls into position pos in the fibonacci sequence.
# The fibonacci sequence is 0 1 1 2 3 5 8... the sequence starts with 0 and 1 and the next number in the sequence is the sum of the two previous. 0 + 1 = 1; 1 + 1 = 2, 1 + 2. = 3, 2 + 3 = 5, 3 + 5 = 8 and so on.
# examples:
#   fib(2) = 1 the number 0 is considered the 0th position in the sequence. 1 is the 1st position and 1 is also the 2nd position.
#   fib(6) = 8
#   fib(10) = 55

num = int(input("Input a number: "))
print(num)
a = 0
b = 1
list = []

for i in range(num):
    list.append([i])
    print(list)




