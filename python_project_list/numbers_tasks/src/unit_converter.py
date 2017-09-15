"""
Unit Converter (temp, currency, volume, mass and more)

Converts various units between one another. The user enters the type of unit being entered,
the type of unit they want to convert to and then the value. The program will then make the conversion.
"""

def convert_temp_celsius_to_fahrenheit(cel):
    return ('From celsius to fahrenheit', float(format(cel * 9 / 5 + 32, '.2f')))

def convert_temp_fahrenheit_to_celsius(far):
    return ('From fahrenheit to celsius', float(format((far - 32) * 5 / 9, '.2f')))

def convert_dollar_to_euro(dollar):
    return ('From euro to dollar', float(format(dollar * 0.83, '.2f')))

def convert_euro_to_dollar(euro):
    return ('From dollar to euro', float(format(euro / 0.83, '.2f')))

def convert_liter_to_gallons(liter):
    return ('From litter to gallons', float(format(liter * 0.26417, '.2f')))

def convert_gallons_to_liter(gallons):
    return ('From gallons to liters', float(format(gallons / 0.26417, '.2f')))

def convert_kilos_to_pounds(kilos):
    return ('From kilos to pounds', float(format(kilos * 2.2046, '.2f')))

def convert_pounds_to_kilos(pound):
    return ('From pounds to kilos', float(format(pound / 2.2046, '.2f')))

conversion_array = [convert_temp_celsius_to_fahrenheit, convert_temp_fahrenheit_to_celsius,
                    convert_dollar_to_euro, convert_euro_to_dollar,
                    convert_liter_to_gallons, convert_gallons_to_liter,
                    convert_kilos_to_pounds, convert_pounds_to_kilos]

start_message = 'Enter option for conversion or (h) for help: '
h = '[1] For celsius to fahrenheit conversion \n'\
    '[2] For fahrenheit to celsius euro \n'\
    '[3] For euro to fahrenheit dollar \n'\
    '[4] For dollar to celsius euro \n' \
    '[5] For litter to gallons dollar \n' \
    '[6] For gallons to litter euro \n' \
    '[7] For kilos to pounds dollar \n' \
    '[8] For pounds to kilos euro \n' \
    '[h] For help \n'\
    '[exit] For exit\n'
enter_value_message = 'Enter value: '

if __name__ == '__main__':
    option = input(start_message)
    while option != 'exit' :
        if (option == 'exit') :
            break
        elif option in '12345678':
            value = float(input(enter_value_message))
            print(*conversion_array[int(option) - 1](value))
        elif option == 'h':
            option = print(h)
        else:
            print(help)
        option = input(start_message)
