from label import *
from addModRem import *


def menu_item(arg):
    while arg.isdigit() != True:
        print('\n Не верный ввод')
        arg = input('Выберите пункт меню: ')
    return int(arg)


def menu():
    notes = []

    while True:
        print("Выберите пунк меню:\n\
              1-Просмотр заметок\n\
              2-Импортировать заметки\n\
              3-Экспортировать заметки\n\
              4-Добавить заметку\n\
              5-Редактировать заметку\n\
              6-Удалить заметку\n\
              0-Выход")
        choice = menu_item(input('Введите значение: '))
        if choice == 1:
            print(f'=========================================')
            printDB(notes)
            print(f'=========================================')
        elif choice == 2:
            print("Импорт")
        elif choice == 3:
            print("Экспорт")
        elif choice == 4:
            print("Добавление")
            notes.append(addNote(notes))
        elif choice == 5:
            print("Редактирование")
        elif choice == 6:
            print("Удаление")
        elif choice == 0:
            print("Программа завереша")
            break
        else:
            print("Выбран несуществующий пункт!")


menu()
