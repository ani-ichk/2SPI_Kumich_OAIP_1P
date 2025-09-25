from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    # обязательный метод для всех подклассов
    def get_permissions(self):
        pass


class AdminUser(User):
    def get_permissions(self):
        return ['читать', 'писать', 'удалять', 'редактировать', 'управлять пользователями']

    def get_user_info(self):
        return 'Доступ к системным настройкам'


class ManagerUser(User):
    def get_permissions(self):
        return ['читать', 'писать', 'редактировать']

    def get_user_info(self):
        return 'Управление товарами'


class GuestUser(User):
    def get_permissions(self):
        return ['читать']

    def get_user_info(self):
        return 'Просмотр каталога'


# Фабрик пользователей
class UserFactory:
    @staticmethod
    def create_user(user_type):
        # возвращает объект пользователя в зависимости от его типа
        if user_type == 'админ':
            return AdminUser()
        elif user_type == 'менеджер':
            return ManagerUser()
        elif user_type == 'гость':
            return GuestUser()
        else:
            return 'Неизвестный тип пользователя'


def main():
    while True:
        user_input = input('Введите тип пользователя: ') # админ менеджер гость

        if user_input:
            if user_input in 'админменеджергость':
                user = UserFactory.create_user(user_input)
                print('Пользователь успешно создан!')
                print(f'Информация: {user.get_user_info()}')
                print(f'Права доступа: {', '.join(user.get_permissions())}')
            else:
                print('Неверный ввод')
        else:
            break


if __name__ == '__main__':
    main()