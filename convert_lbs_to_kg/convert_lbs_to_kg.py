#  enter weight in lbs or kg and convert it to the other unit.

weight = int(input("Enter your weight: "))
weight_in = input("(L)bs or(K)g: ")
converted_wt = 0.0

if weight_in == "L":
    converted_wt = weight * 0.45
elif weight_in == "K":
    converted_wt = weight * 2.2
print(converted_wt)
