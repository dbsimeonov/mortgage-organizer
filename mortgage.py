import json
from prettytable import PrettyTable

from helpers import calc_mortgage, print_mortgage_deal


with open('data.json') as json_file:
    data = json.load(json_file)

if len(data['data']):
    uuid = max([obj.get('id') for obj in data['data']]) + 1
else:
    uuid = 1

principal = int(input('Principal of mortgage:  '))
deposit = int(principal * 0.3)
principal = int(principal * (1-0.3))
interest = float(input('Interest rate:  ')) # 3.7
years = int(input('Years:  '))  # 25
monthly_payment = calc_mortgage(principal, interest, years)
total_amount = monthly_payment * years * 12

print_mortgage_deal(years, principal, interest, monthly_payment, total_amount)

calc_row = {
    'id': uuid,
    'years': years,
    'deposit': deposit,
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

table = PrettyTable(['ID', 'Y', 'IR', 'Dep', 'Loan', 'MPM', 'Total'])
for obj in json_data_updated['data']:
   table.add_row([
      obj.get('id') or '<null>',
      obj.get('years') or '<null>',
      obj.get('interest') or '<null>',
      '£{:,}'.format(obj.get('deposit')) or '<null>',
      '£{:,}'.format(obj.get('loan')) or '<null>',
      '£{:,}'.format(obj.get('monthly')) or '<null>',
      '£{:,}'.format(obj.get('total_amount')) or '<null>',
   ])

print(table)
