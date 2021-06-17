
year = int(input("Input a year: "))

if(year %4 == 0 and year %100 != 0):
    print("True")
elif(year %4 == 0 and year %400 != 0):
    print("False")



