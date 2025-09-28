from abc import  ABC, abstractmethod

# Интерфейс (абстрактный класс) для стратегии оплаты
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Конкретные стратегии оплаты
# Кредитная карта
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'💳 Оплата кредитной картой на сумму {amount} руб')
        if amount > 3000:
            pin = int(input('Введите PIN-код: '))
            # проверка кода ...
        print('Оплата прошла')


# Электронные деньги
class EWalletPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'📱 Оплата электронными деньгами на сумму {amount} руб')
        code = int(input('Введите код из СМС: '))
        # проверка кода ...
        print('Оплата прошла')


# Наличные
class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'💵 Оплата наличными на сумму {amount} руб')
        print('Оплата прошла')


class PaymentContext:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy # устанавливаем стратегию оплаты

    def execute(self, amount):
        if self.strategy is None:
            return 'Ошибка! сначала выберите способ оплаты'
        return self.strategy.pay(amount) # выполняем оплату используя выбранную стратегию


def main():
    terminal = PaymentContext()

    amount = float(input('Введите сумму оплаты: '))

    strategies = {
        '1': CreditCardPayment(),
        '2': EWalletPayment(),
        '3': CashPayment()
    }

    while True:
        print('\nСпособы оплаты:')
        print('1 - 💳 Кредитная карта')
        print('2 - 📱 Электронные деньги')
        print('3 - 💵 Наличные')

        choice = input('\nВыберите способ оплаты (1-3): ')

        if choice in strategies:
            terminal.set_strategy(strategies[choice])  # устанавливаем стратегию
            terminal.execute(amount)  # выполняем оплату
        else:
            print('Неверный ввод!')
            break


if __name__ == '__main__':

    main()
