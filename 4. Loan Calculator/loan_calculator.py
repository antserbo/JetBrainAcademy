import math
import argparse

parser = argparse.ArgumentParser(description='This program is used to calculate ')
parser.add_argument('--type', type=str, metavar='', help='Differentiated or Annuity')
parser.add_argument('--principal', type=int, metavar='', help='The loan principal')
parser.add_argument('--periods', type=int, metavar='', help='Number of payments')
parser.add_argument('--interest', type=float, metavar='', help='Nominal interest rate')
parser.add_argument('--payment', type=int, metavar='', help='Monthly payment amount')
args = parser.parse_args()


def calculate_differentiated_payments(loan_interest, loan_principal, number_of_periods):
    credit_payout = 0
    for n in range(1, number_of_periods + 1):
        i = loan_interest / 1200
        differentiated_payment = loan_principal / number_of_periods + i * (
                loan_principal - (loan_principal * (n - 1) / number_of_periods))
        print(f'Math {n} payment is {math.ceil(differentiated_payment)}')
        credit_payout += math.ceil(differentiated_payment)
    print(f'\nOverpayment = {credit_payout - loan_principal}')


def calculate_annuity_payment(loan_principal, number_of_periods, loan_interest):
    ordinary_annuity = loan_principal * ((loan_interest / 1200) * (1 + loan_interest / 1200) ** number_of_periods) / (
            (1 + loan_interest / 1200) ** number_of_periods - 1)

    print(f'Your monthly payment = {math.ceil(ordinary_annuity)}!')
    print(f'Overpayment = {math.ceil(ordinary_annuity) * number_of_periods - loan_principal}')


def calculate_principal(annuity_payment, number_of_periods, loan_interest):
    loan_principal = annuity_payment / (((loan_interest / 1200) * (1 + loan_interest / 1200) ** number_of_periods) / (
            (1 + loan_interest / 1200) ** number_of_periods - 1))

    print(f'Your loan principal = {math.floor(loan_principal)}!')
    print(f'Overpayment = {math.ceil(annuity_payment * number_of_periods - loan_principal)}')


def calculate_periods(loan_principal, monthly_payment, loan_interest):
    number_of_monthly_payments = math.log((monthly_payment / (monthly_payment - loan_interest / 1200 * loan_principal)),
                                          (1 + loan_interest / 1200))

    completed_months = math.ceil(number_of_monthly_payments)

    if completed_months % 12 == 0 and completed_months // 12 != 0:
        if completed_months // 12 == 1:
            print('It will take 1 year to repay this loan!')
        else:
            print(f'It will take {completed_months // 12} years to repay this loan!')
    elif completed_months // 12 == 0 and completed_months % 12 != 0:
        if completed_months == 1:
            print('It will take 1 month to repay this loan!')
        else:
            print(f'It will take {completed_months} months to repay this loan!')
    else:
        years = completed_months // 12
        months = completed_months - 12 * years
        print(f'It will take {years} years and {months} to repay this loan!')

    print(f'Overpayment = {monthly_payment * completed_months - loan_principal}')


if args.type == 'diff' and args.principal and args.periods and args.interest:
    if args.principal > 0 and args.periods > 0 and args.interest > 0:
        calculate_differentiated_payments(args.interest, args.principal, args.periods)
    else:
        print('Incorrect parameters.')
elif args.type == 'annuity' and args.principal and args.periods and args.interest:
    if args.principal and args.periods > 0 and args.interest > 0:
        calculate_annuity_payment(args.principal, args.periods, args.interest)
    else:
        print('Incorrect parameters.')
elif args.type == 'annuity' and args.payment and args.periods and args.interest:
    if args.payment and args.periods and args.interest:
        calculate_principal(args.payment, args.periods, args.interest)
    else:
        print('Incorrect parameters.')
elif args.type == 'annuity' and args.principal and args.payment and args.interest:
    if args.principal > 0 and args.payment > 0 and args.interest > 0:
        calculate_periods(args.principal, args.payment, args.interest)
    else:
        print('Incorrect parameters.')

else:
    print('Incorrect parameters.')