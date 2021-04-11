#  use logical operators for multiple conditions

# logical and operator   applicant has high income AND good credit.


has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("eligible for loan")

# logical and operator   applicant has high income OR good credit, one condition should be true.

if has_high_income or has_good_credit:
    print("eligible for loan")

# if applicant has good credit and doesn't have a criminal record, is eligible.

if has_good_credit and not has_criminal_record:
    print("eligible for loan")