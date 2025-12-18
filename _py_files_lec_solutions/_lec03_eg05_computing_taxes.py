"""
The US federal personal income tax is calculated based on the filing status and taxable income. 
Suppose we look at just one filing status: 
    single filers 
Example tax rates for are shown below.
+----------------------+-----------------------+---------------------------------+
| Taxable Income Range | Single Filer Rate (%) | Married Filing Jointly Rate (%) |
+----------------------+-----------------------+---------------------------------+
| $0 - $9,950          | 10                    | 10                              |
| $9,951 - $40,525     | 12                    | 12                              |
| $40,526 - $86,375    | 22                    | 22                              |
| $86,376 - $164,925   | 24                    | 24                              |
| $164,926 - $209,425  | 32                    | 32                              |
| $209,426 - $523,600  | 35                    | 35                              |
| Over $523,600        | 37                    | 37                              |
+----------------------+-----------------------+---------------------------------+


"""
#imports
import sys


#function defs
def calculate_tax(income, status):
    if status == 'single':
        brackets = [0, 9875, 40125, 85525, 163300, 207350, 518400]
        rates = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    elif status == 'married':
        brackets = [0, 19750, 80250, 171050, 326600, 414700, 622050]
        rates = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    else:
        raise ValueError("Invalid filing status")

    tax = 0
    prev_bracket = 0

    for i in range(len(brackets)):
        if income <= brackets[i]:
            tax += (income - prev_bracket) * rates[i]
            break
        else:
            tax += (brackets[i] - prev_bracket) * rates[i]
            prev_bracket = brackets[i]

    return tax


#Code using above imports and defs
# Prompt the user to enter filing status
status = input("Enter the filing status: ")

# Prompt the user to enter taxable income
income = float(input("Enter the taxable income: "))

# Compute tax
tax = 0
# # Example Enter values for a single filer with an income of $40,000
# income = 40000
# status = 'single'
tax = calculate_tax(income, status)
print(f'Tax for a {status} filer with an income of {income}: {tax:.2f}')

