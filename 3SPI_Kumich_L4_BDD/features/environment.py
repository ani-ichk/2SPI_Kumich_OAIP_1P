def before_scenario(context, scenario):
    # инициализируем структуру для хранения данных теста
    context.test_data = {
        'app': None,  # ссылка на приложение qt
        'window': None,  # ссылка на главное окно
        'db': None,  # ссылка на базу данных
        'cats_count': 0  # счетчик котов для отслеживания изменений
    }


def after_scenario(context, scenario):
    # очищаем ресурсы, если они были созданы
    if context.test_data['window']:
        try:
            context.test_data['window'].close()
        except:
            pass  # если окно уже закрыто, ничего не делаем

    if context.test_data['db']:
        try:
            # закрываем соединение с базой данных
            context.test_data['db'].close()
        except:
            pass

    # очищаем данные контекста
    context.test_data.clear()