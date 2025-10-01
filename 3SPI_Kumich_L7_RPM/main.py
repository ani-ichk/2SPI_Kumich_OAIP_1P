def require_admin(func):
    def wrapper(user_id):
        if user_id['роль'] == 'администратор':
            return func(user_id)
        return 'Ошибка: недостаточно прав!'
    return wrapper


@require_admin
def delete_user(user_id):
    return f'Пользователь удален администратором {client['имя']}'


admin = {'роль': 'администратор',
         'имя': 'Александр',
         'возраст': '40'}
client = {'роль': 'клиент',
        'имя': 'Михаил',
        'возраст': '30'}

print(delete_user(admin))  # работает
print(delete_user(client))   # ошибка прав