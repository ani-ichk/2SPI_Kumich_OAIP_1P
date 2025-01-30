def brackets(s):
    stack = [] # список, хранящий пока не закрытые скобки
    # цикл, проходящий по каждому эл-ту строки
    for i in s:
        # если открывающая скобка, добавляем в список стек
        if i in ('(', '[', '{', '<'):
            stack.append(i)
            continue
        if not stack:
            return False
        # если закрывающая скобка - проверяем на наличие второй пары
        need = ''
        if i == ')':
            need = '('
        elif i == ']':
            need = '['
        elif i =='}':
            need = '{'
        elif i == '>':
            need = '<'
        if stack[-1] == need:
            stack.pop(-1)
    return not stack
