import logging
logging.basicConfig(level=logging.DEBUG)

values = []


def dodawanie(value_1, value_2):
    print(value_1 + value_2)


def odejmowanie(value_1, value_2):
    print(value_1 - value_2)


def mnozenie(values):
    result = 1
    for v in values:
        result = result * int(v)
    print(f'Wynik to {result}')


def dzielenie(values):
    result = int(values[0])
    del values[0]
    for v in values:
        result = result / int(v)
    print(f'Wynik to {result}')


if __name__ == "__main__":
    calculation_type = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:')
    if calculation_type == '1' or calculation_type == '2':
        value_1 = input('Podaj pierwszą wartosc: ')
        value_2 = input('Podaj drugą wartosc: ')

        if value_1.isdigit() and value_2.isdigit():
            if calculation_type == '1':
                logging.info('Dodaję ' + value_1 + " i " + value_2)
                dodawanie(int(value_1), int(value_2))
            elif calculation_type == '2':
                logging.info('Odejmuje od ' + value_1 + " liczbę " + value_2)
                odejmowanie(int(value_1), int(value_2))
        else:
            print('Tylko wartosci liczbowe!')

    if calculation_type == '3' or calculation_type == '4':
        while True:
            value = input('Podaj liczbę lub wpisz Y zeby obliczyc: ')
            if value == str.lower('y'):
                break
            else:
                values.append(value)
        if len(values) < 2:
            print('Podaj przynajmniej dwie liczby')
        else:
            if calculation_type == '3':
                mnozenie(values)
            elif calculation_type == '4':
                dzielenie(values)
