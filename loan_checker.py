
annual_income = int(input("Enter annual income: "))
credit_score = int(input("Enter credit score: "))

if annual_income > 30000:
    has_good_income = True
else:
    has_good_income = False

if 628 < credit_score < 710:
    credit_status = "Excellent"
elif 604 < credit_score < 627:
    credit_status = "Good"
elif 566 < credit_score < 603:
    credit_status = "Ok"
elif 551 < credit_score < 565:
    credit_status = "Needs some work"
elif 300 < credit_score < 550:
    credit_status = "Needs work"
else:
    print("Failed to find your credit score!")


if credit_status == "Excellent" or credit_status == "Good":
    has_good_credit = True
else:
    has_good_credit = False


if has_good_income and has_good_credit:
    credit_check_message = "Eligible for loan, Max upto £30,000"
elif has_good_income and credit_status == "Ok":
    credit_check_message = "Eligible for loan, Max upto £15,000"
elif has_good_credit and not has_good_income:
    credit_check_message = "Eligible for loan, Max upto £10,000"
elif credit_status == "Needs some work":
    credit_check_message = "Eligible for loan, Max up to £300"
elif credit_status == "Needs work":
    credit_check_message = "Not Eligible for loan at this moment!"
else:
    print("There was a problem, Try again later!")

print(f"Final decision: {credit_check_message}")
