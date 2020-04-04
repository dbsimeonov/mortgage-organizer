import json
from prettytable import PrettyTable

from helpers import calc_mortgage, print_mortgage_deal


with open('data.json') as json_file:
    data = json.load(json_file)

uuid = max([obj.get('id') for obj in data['data']]) + 1

principal = int(int(input('Principal of mortgage:  ')) / 1.3)
interest = float(input('Interest rate:  ')) # 3.7
years = int(input('Years:  '))  # 25
monthly_payment = calc_mortgage(principal, interest, years)
total_amount = monthly_payment * years * 12

print_mortgage_deal(years, principal, interest, monthly_payment, total_amount)

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

table = PrettyTable(['ID', 'Y', 'Int', 'Loan', 'MPM', 'Total'])
for obj in json_data_updated['data']:
   table.add_row([
      obj.get('id'),
      obj.get('years'),
      obj.get('interest'),
      '£{:,}'.format(obj.get('loan')),
      '£{:,}'.format(obj.get('monthly')),
      '£{:,}'.format(obj.get('total_amount')),
   ])

print(table)
