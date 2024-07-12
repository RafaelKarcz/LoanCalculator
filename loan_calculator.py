import argparse
import math
import sys

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print('Incorrect Parameters')
        sys.exit(2)

def positive_number(value):
    """
    Ensuring the value is a positive number.
    """
    try:
        input_value = float(value)
        if input_value <= 0:
            raise argparse.ArgumentTypeError()
        return input_value
    except ValueError:
        raise argparse.ArgumentTypeError()

def is_invalid_args(args):
    """
    Check if the provided arguments are valid based on the type of calculation.
    """
    # Check for required interest
    if args.interest is None:
        return True
    
    # Annuity type specific checks
    if args.type == 'annuity':
        if not ((args.payment and args.periods) or 
                (args.payment and args.principal) or 
                (args.principal and args.periods)):
            return True

    # Differentiated type specific checks
    if args.type == 'diff':
        if args.principal is None or args.periods is None:
            return True

    return False

def calculate_monthly_payment(principal, annual_interest_rate, total_periods):
    """
    Calculate the monthly payment amount based on the loan principal, 
    annual interest rate, and total number of payments.
    """
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    compound_interest_factor = pow((1 + monthly_interest_rate), total_periods)
    monthly_payment = math.ceil(principal * (monthly_interest_rate * compound_interest_factor) / (compound_interest_factor - 1))
    total_payments = monthly_payment * total_periods
    overpayment = round(total_payments - principal)
    return monthly_payment, overpayment
    
def calculate_loan_principal(monthly_payment, annual_interest_rate, total_periods):
    """
    Calculate the loan principal based on the monthly payment, 
    annual interest rate, and total number of payments.
    """
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    compound_interest_factor = pow((1 + monthly_interest_rate), total_periods)
    principal = int(monthly_payment / (monthly_interest_rate * compound_interest_factor / (compound_interest_factor - 1)))
    total_payments = monthly_payment * total_periods
    overpayment = int(total_payments - principal)
    return principal, overpayment

def calculate_number_of_payments(monthly_payment, annual_interest_rate, principal):
    """
    Calculate the number of payments required to repay the loan based on 
    the monthly payment, loan principal, and annual interest rate.
    """
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    number_of_payments = math.log(monthly_payment / (monthly_payment - monthly_interest_rate * principal), 1 + monthly_interest_rate)
    total_payments = monthly_payment * math.ceil(number_of_payments)
    overpayment = round(total_payments - principal)
    return math.ceil(number_of_payments), overpayment

def calculate_differentiated_payments(principal, annual_interest_rate, total_periods):
    """
    Calculate differentiated payments based on the loan principal,
    annual interest rate, and number of payment periods.
    """
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    total_payments = 0
    for month in range(1, int(total_periods) + 1):
        monthly_interest = monthly_interest_rate * (principal - (principal * (month - 1) / total_periods))
        differentiated_payment = math.ceil(principal / total_periods + monthly_interest)
        print(f'Month {month}: payment is {differentiated_payment}')
        total_payments += differentiated_payment
    overpayment = round(total_payments - principal)
    print(f'Overpayment = {overpayment}')

def annuity_calculations(args):
    """
    Calculate and print results for annuity based loans.
    """
    if args.principal and args.periods:
        monthly_payment, overpayment = calculate_monthly_payment(args.principal, args.interest, args.periods)
        print(f'Your monthly payment = {monthly_payment}!')
        print(f'Overpayment = {overpayment}')
    elif args.payment and args.periods:
        principal, overpayment = calculate_loan_principal(args.payment, args.interest, args.periods)
        print(f'Your loan principal = {principal}!')
        print(f'Overpayment = {overpayment}')
    elif args.payment and args.principal:
        number_of_payments, overpayment = calculate_number_of_payments(args.payment, args.interest, args.principal)
        print_time_to_repay(number_of_payments)
        print(f'Overpayment = {overpayment}')

def differentiated_calculations(args):
    """
    Calculate and print results for differentiated payment loans.
    """
    if args.principal and args.periods:
        calculate_differentiated_payments(args.principal, args.interest, args.periods)

def print_time_to_repay(number_of_payments):
    """
    Print time to repay the loan in years and months based on total number of payments.
    """
    if number_of_payments % 12 == 0:
        years = number_of_payments / 12
        print(f'It will take {int(years)} years to repay this loan!')
    elif number_of_payments > 12:
        years = number_of_payments // 12
        months = number_of_payments % 12
        print(f'It will take {int(years)} years and {int(months)} months to repay this loan!')
    else:
        print(f'It will take {int(number_of_payments)} months to repay this loan!')

def main():
    """
    Main function to handle user interactions via the argparse module.
    Parses user input and invokes appropriate calculations based on the loan type.
    """
    parser = CustomArgumentParser(description='Calculate loan payments.')
    parser.add_argument('--payment', type=positive_number, help='Monthly payment amount.')
    parser.add_argument('--principal', type=positive_number, help='Loan principal amount.')
    parser.add_argument('--periods', type=positive_number, help='Total number of repayment periods.')
    parser.add_argument('--interest', type=positive_number, required=True, help='Annual interest rate (without the percentage sign).')
    parser.add_argument('--type', type=str, required=True, choices=['annuity', 'diff'], help='Type of calculation: annuity or differentiated payments.')

    args = parser.parse_args()

    if is_invalid_args(args):
        print('Incorrect Parameters')
        sys.exit(2)

    if args.type == 'annuity':
        annuity_calculations(args)
    elif args.type == 'diff':
        differentiated_calculations(args)

if __name__ == '__main__':
    main()