import numpy as np

def luhn_validation_algorithm(card_number):
    card_number_array = list(card_number)
    card_number_array = [int(card_number_array[j]) for j in range(0,len(card_number_array))]
    check_digit = card_number_array[len(card_number_array)-1]
    card_number_array = card_number_array[:len(card_number_array)-1]
    card_number_array = np.array(card_number_array)
    card_number_array = card_number_array[::-1]
    card_number_array[::2] *= 2
    card_number_array = np.array([card_number_array[i] - (0 if (i % 2 == 1) or card_number_array[i] < 9 else 9)
                         for i in range(0, len(card_number_array))])
    return (sum(card_number_array) * 9) % 10 == check_digit

if __name__ == '__main__':
    print(luhn_validation_algorithm("4556737586899855"))
    print(luhn_validation_algorithm("4716537222222112"))
    print(luhn_validation_algorithm("5020843942608959"))