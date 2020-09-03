import logging
logging.basicConfig(level=logging.DEBUG)


def dodawanie(value_1, value_2):
    print(value_1 + value_2)

def odejmowanie(value_1, value_2):
    print(value_1 - value_2)

def mnozenie(value_1, value_2):
    print(value_1 * value_2)

def dzielenie(value_1, value_2):
    print(value_1 / value_2)

if __name__ == "__main__":
    calculation_type = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:')
    value_1 = input('podaj pierwszą wartosc: ')
    value_2 = input('podaj drugą wartosc: ')

    if value_1.isdigit() and value_2.isdigit():
        if calculation_type == '1':
         logging.info('Dodaję ' + value_1 + " i " + value_2)
         dodawanie(int(value_1), int(value_2))
        elif calculation_type == '2':
         logging.info('Odejmuje ' + value_1 + " i " + value_2)
         odejmowanie(int(value_1), int(value_2))
        elif calculation_type == '3':
         logging.info('Mnożę ' + value_1 + " razy " + value_2)
         mnozenie(int(value_1), int(value_2))
        elif calculation_type == '4':
         logging.info('Dzielę ' + value_1 + " przez " + value_2)
         dzielenie(int(value_1), int(value_2))
    else:
        print('You entered non numeric values!')
