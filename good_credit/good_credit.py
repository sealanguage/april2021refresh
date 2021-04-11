price = 1000000
good_credit = False


if good_credit:
    downpayment = .10 * price
else:
    downpayment = 0.2 * price
print(f"down payment : ${downpayment}")