import math

def calc_mortgage(principal, interest, years):
    '''
    given mortgage loan principal, interest(%) and years to pay
    calculate and return monthly payment amount
    '''
    # monthly rate from annual percentage rate
    interest_rate = interest/(100 * 12)
    # total number of payments
    payment_num = years * 12
    # calculate monthly payment
    payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
    return payment

def print_mortgage_deal(years, principal, interest, monthly_payment, total_amount):
    sf = '''\
For a {} year mortgage loan of ${:,}
at an annual interest rate of {:.2f}%
you pay ${:.2f} monthly'''
    print('-'*55)
    print(sf.format(years, principal, interest, monthly_payment))
    print('-'*55)
    print("Total amount paid will be ${:,.2f}".format(total_amount))

# from operator import itemgetter
# sorted_list = sorted(d, key=itemgetter('total_amount')
