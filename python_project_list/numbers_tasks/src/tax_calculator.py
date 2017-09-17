tax_rates = {
    'Ukraine': 0.13,
    'USA' : 0.2,
    'England' : 0.3,
    'Germany' : 0.1,
    'France' : 0.05
}
def calculate_tax_rate():
    print('Do you want to enter tax rate[1] or country[2]?')
    option = int(input())

    cost = float(input('Input enter a cost: '))
    if option == 2:
        country = input('Enter a country: ')
        tax = tax_rates[country]
        tuple_for_print = (country, tax_rates[country], cost + tax * cost)
    else :
        tax = float(input('Enter a tax rate '))
        tuple_for_print = (tax, cost + tax * cost)

    return tuple_for_print

