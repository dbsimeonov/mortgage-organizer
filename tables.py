from prettytable import PrettyTable

def display_table(data):
    table = PrettyTable(['ID', 'Y', 'IR', 'Dep', 'Loan', 'MPM', 'Total'])
    for obj in data:
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
