dateReturned = input().split()
dateDue = input().split()

dateReturnedDay = dateReturned[0]
dateReturnedMonth = dateReturned[1]
dateReturnedYear = dateReturned[2]

dateDueDay = dateDue[0]
dateDueMonth = dateDue[1]
dateDueYear = dateDue[2]

daysLate = int(dateReturnedDay) - int(dateDueDay)

monthsLate = int(dateReturnedMonth) - int(dateDueMonth)

yearsLate = int(dateReturnedYear) - int(dateDueYear)
# print(yearsLate)

if (yearsLate > 0):
    print(10000)

elif (yearsLate < 0):
    print(0)

elif (monthsLate > 0):
    print(monthsLate * 500)

elif (daysLate > 0):
    print(daysLate * 15)

else:
    print(0)

