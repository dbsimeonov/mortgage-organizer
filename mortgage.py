import json
from prettytable import PrettyTable

from helpers import calc_mortgage


with open('data.json') as json_file:
    data = json.load(json_file)

uuid = max([obj.get('id') for obj in data['data']]) + 1

principal = int(80000 / 1.3)
interest = 4.1
years = 25
monthly_payment = calc_mortgage(principal, interest, years)
total_amount = monthly_payment * years * 12

sf = '''\
For a {} year mortgage loan of ${:,}
at an annual interest rate of {:.2f}%
you pay ${:.2f} monthly'''
print(sf.format(years, principal, interest, monthly_payment))
print('-'*58)
print("Total amount paid will be ${:,.2f}".format(total_amount))

calc_row = {
    'id': uuid,
    'years': years,
    'loan': principal,
    'interest': interest,
    'monthly': int(monthly_payment),
    'total_amount': int(total_amount),
}

def write_json(data, filename='data.json'):
   with open(filename, 'w') as f:
      json.dump(data, f, indent=4)

with open('data.json') as json_file:
    data['data'].append(calc_row)

write_json(data)

# Get updated data
with open('data.json') as json_file:
    json_data_updated = json.load(json_file)

table = PrettyTable(['Id', 'Years', 'Loan', 'Interest', 'Monthly', 'Total Amount'])
for obj in json_data_updated['data']:
   table.add_row([
      obj.get('id'),
      obj.get('years'),
      obj.get('loan'),
      obj.get('interest'),
      obj.get('monthly'),
      obj.get('total_amount')
   ])

print(table)