#! /usr/bin/env python


def income_tax(income):
    single_tax_brackets = {
            11600: .1,
            47150: .12,
            100525: .22,
            191950: .24,
            243725: .32,
            609350: .35,
            609351: .37,
            }
    # Insert Other Brackets

    tax = 0

    # Federal Taxes
    if income < 11600:
        tax = income * single_tax_brackets[11600]
    for bracket, rate in single_tax_brackets.items():
        if income >= bracket and (income - bracket) > 0:
            tax += min(bracket, income - bracket) * rate
        else:
            break
    # Social Security Taxes https://www.irs.gov/taxtopics/tc751
    # Medicare https://www.irs.gov/taxtopics/tc751

    # State Taxes

    return tax

money = 10000
firstTry = income_tax(money)
print(f"Your income tax is {firstTry} and your income after federal taxes is {money - firstTry}")

money = 50000
firstTry = income_tax(money)
print(f"Your income tax is {firstTry} and your income after federal taxes is {money - firstTry}")

money = 72000
firstTry = income_tax(money)
print(f"Your income tax is {firstTry} and your income after federal taxes is {money - firstTry}")

money = 80000
firstTry = income_tax(money)
print(f"Your income tax is {firstTry} and your income after federal taxes is {money - firstTry}")
