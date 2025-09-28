from abc import ABC, abstractmethod


# (Реализация) интерфейс для валют - определяет КАК работать с деньгами
class Currency(ABC):
    @abstractmethod
    def convert_amount(self, amount):
        """ КАК форматировать сумму денег """
        pass

    @abstractmethod
    def get_currency_code(self):
        """ КАК получить код валюты """
        pass


# Реализуем конкретные валюты
class USDCurrency(Currency):
    def convert_amount(self, amount):
        # в реальности здесь была бы логика конвертации, но мы просто возвращаем
        return f'{amount}$'

    def get_currency_code(self):
        return 'USD'


class EURCurrency(Currency):
    def convert_amount(self, amount):
        return f'{amount}€'

    def get_currency_code(self):
        return 'EUR'


# Абстракция для транзакций - определяет ЧТО делать
class Transaction(ABC):
    def __init__(self, currency):
        # МОСТ: транзакция связана с валютой (currency - об-т валюты)
        self.currency = currency  # "МОСТ" - связываем транзакцию с валютой

    @abstractmethod
    def execute(self, amount):
        """ ЧТО нужно сделать - выполнить транзакцию """
        pass


# Конкретные транзакции (уточненные абстракции)
class BankTransfer(Transaction):
    def execute(self, amount):
        # мост к валюте для форматирования суммы
        formatted_amount = self.currency.convert_amount(amount)

        return f'''   БАНКОВСКИЙ ПЕРЕВОД:
   Сумма: {formatted_amount}
   Валюта: {self.currency.get_currency_code()}
   Статус: Перевод выполнен успешно!'''


class MobileAppTransfer(Transaction):
    def execute(self, amount):
        formatted_amount = self.currency.convert_amount(amount)

        return f'''   МОБИЛЬНЫЙ ПЕРЕВОД:
   Сумма: {formatted_amount}  
   Валюта: {self.currency.get_currency_code()}
   Статус: Перевод выполнен успешно!'''


def main():
    amount = float(input('Введите сумму для перевода: '))

    currencies = {
        '1': USDCurrency(),
        '2': EURCurrency()
    }

    transactions = {
        '1': BankTransfer,
        '2': MobileAppTransfer
    }

    while True:
        currency_choice = input('''Выберите валюту:
    1 - USD
    2 - EUR\n''')
        if currency_choice not in currencies:
            print('Неправильный выбор валюты!')
            continue

        transaction_choice = input('''Выберите тип перевода:
    1 - банковский перевод
    2 - мобильный перевод\n''')
        if transaction_choice not in transactions:
            print('Неправильный выбор типа перевода!')
            continue

        # создаем транзакцию с выбранной валютой
        selected_currency = currencies[currency_choice]
        selected_transaction = transactions[transaction_choice]

        # соединяем тип транзакции с валютой
        transaction = selected_transaction(selected_currency)

        # выполняем транзакцию
        result = transaction.execute(amount)
        print(result)

        continue_choice = input('Попробовать другую комбинацию?: ')
        if continue_choice == 'нет':
            print('Выход из программы')
            break


if __name__ == '__main__':
    main()