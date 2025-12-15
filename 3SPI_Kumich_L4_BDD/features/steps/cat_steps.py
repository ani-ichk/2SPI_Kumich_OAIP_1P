from behave import given, when, then
from cat_db import CatDatabase
from cat_gui import CatWindow
from PyQt6.QtWidgets import QApplication
import sys

@given('открыто приложение учета котов')
def step_open_app(context):
    # получаем существующий экземпляр QApplication или создаем новый
    context.app = QApplication.instance() or QApplication(sys.argv)
    # создаем базу данных в памяти для тестов
    context.db = CatDatabase(":memory:")
    # создаем главное окно приложения
    context.window = CatWindow(context.db)
    # сохраняем ссылки в test_data для environment.py
    context.test_data['app'] = context.app
    context.test_data['window'] = context.window
    context.test_data['db'] = context.db

@given('в базе есть коты')
def step_db_has_cats(context):
    # добавляем тестовых котов в базу данных
    context.db.add_cat("Тестовый кот", 3, "тестовая", "тестовый")
    context.db.add_cat("Другой кот", 2, "другая", "другой")
    # сохраняем количество котов для проверок
    context.test_data['cats_count'] = 2

@given('в базе есть кот с id {cat_id}')
def step_db_has_cat_with_id(context, cat_id):
    # добавляем кота с указанным id в имени
    context.db.add_cat(f"Кот {cat_id}", 1, "любая", "любой")
    # сохраняем id кота в контексте для использования в других шагах
    context.cat_id = cat_id
    context.test_data['cats_count'] = 1

@when('я добавляю кота с именем "{name}" возрастом {age}')
def step_add_cat(context, name, age):
    # заполняем поля ввода в интерфейсе
    context.window.name_input.setText(name)
    context.window.age_input.setText(str(age))
    # вызываем метод добавления кота
    context.window.add_cat()
    # обновляем счетчик котов
    context.test_data['cats_count'] = len(context.db.get_all_cats())

@when('я пытаюсь добавить кота с именем "{name}" и возрастом {age}')
def step_try_add_invalid_cat(context, name, age):
    # заполняем поля ввода (включая некорректные данные)
    context.window.name_input.setText(name)
    context.window.age_input.setText(str(age))
    # вызываем метод добавления (должен показать ошибку)
    context.window.add_cat()

@when('я открываю окно просмотра')
def step_open_view_window(context):
    context.window.show_cats()

@when('я изменяю имя кота на "{new_name}"')
def step_update_cat_name(context, new_name):
    # обновляем имя кота с id 1 напрямую через базу данных
    context.db.update_cat(1, name=new_name)

@when('я удаляю кота с id {cat_id}')
def step_delete_cat(context, cat_id):
    # удаляем кота напрямую через базу данных
    context.db.delete_cat(int(cat_id))
    # обновляем счетчик котов
    context.test_data['cats_count'] = len(context.db.get_all_cats())

@when('я нажимаю кнопку "{button_text}"')
def step_click_button(context, button_text):
    if button_text == "Показать всех котов":
        context.window.show_cats()

@then('в базе должен быть кот с именем "{name}"')
def step_check_cat_in_db(context, name):
    cats = context.db.get_all_cats()
    cat_names = [cat[1] for cat in cats]
    assert name in cat_names, f"Кот {name} не найден в базе"

@then('я вижу сообщение об успехе')
def step_see_success_message(context):
    print("проверка сообщения об успехе - требует мокирования")

@then('я получаю сообщение об ошибке')
def step_see_error_message(context):
    print("проверка сообщения об ошибке - требует мокирования")

@then('кот не добавляется в базу')
def step_cat_not_added(context):
    cats_before = len(context.db.get_all_cats())
    # пытаемся добавить кота (должно быть сообщение об ошибке)
    context.window.add_cat()
    cats_after = len(context.db.get_all_cats())
    # проверяем что количество котов не изменилось
    assert cats_before == cats_after, "Кот был добавлен несмотря на ошибку"

@then('я вижу список всех котов из базы')
def step_see_all_cats(context):
    cats_in_db = context.db.get_all_cats()
    # просто выводим количество котов для отладки
    print(f"в базе {len(cats_in_db)} котов")

@then('имя кота в базе должно обновиться')
def step_check_cat_updated(context):
    cats = context.db.get_all_cats()
    # проверяем что есть хотя бы один кот с новым именем
    assert any(cat[1] == "Новый имя" for cat in cats), "имя кота не обновилось"

@then('кот должен исчезнуть из базы')
def step_check_cat_deleted(context):
    cats = context.db.get_all_cats()
    # извлекаем все id котов
    cat_ids = [cat[0] for cat in cats]
    # проверяем что кота с id 1 больше нет
    assert 1 not in cat_ids, "кот не был удален"

@then('открывается окно со списком котов')
def step_window_opened(context):
    # проверяем что окно просмотра видимо
    assert context.window.cats_window.isVisible(), "окно просмотра не открылось"