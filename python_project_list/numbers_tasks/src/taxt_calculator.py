tax_rates = {
    'Ukraine': 0.13,
    'USA' : 0.2,
    'England' : 0.3,
    'Germany' : 0.1,
    'France' : 0.05
}
print('Do you want to enter tax rate[1] or country[2]?')
option = int(input())

cost = float(input('Input enter a cost: '))
if option== 2:
    country = input('Enter a country: ')
    tax = tax_rates[country]
    message = 'Tax rate for %s is %.2f. Cost with tax is %.2f'
    tuple_for_print = (country, tax_rates[country], cost + tax * cost)
else :
    tax = float(input('Enter a tax rate '))
    message = 'Tax rate is %.2f. Cost with tax is %.2f'
    tuple_for_print = (tax, cost + tax * cost)

print (message % tuple_for_print)

