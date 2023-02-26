from label import *

import datetime


def menu_item(arg):
    while arg.isdigit() != True:
        print('\n Не верный ввод')
        arg = input('Введите корректное значене: ')
    return int(arg)


def addNote(notes):
    noteTemp = inputNote(notes)
    return Label(noteTemp[0], noteTemp[1], noteTemp[2], noteTemp[3])


def editNote(notes):
    if (len(notes) > 0):
        tempId = input("Введите id заметки: ")
        i = menu_item(tempId)
        if i < len(notes):
            notes[i] = addNote(notes)
            print(f'=========================================')
            print("Изменение сохраниено")
            print(f'=========================================')
        else:
            print('Заметки с таким номером не существует!')
    else:
        print('Список заметок пуст!!')


def inputNote(notes):
    idTemp = len(notes)
    title = input("Введите заголовок: ")
    text = input("Введите текст заметки: ")
    date = datetime.datetime.now()
    return [title, text, date.strftime("%d.%m.%Y %H:%M"), idTemp]


def printDB(data):
    if len(data) > 0:
        for object in data:
            print(f'=========================================')
            print(object.info())
            print(f'=========================================')
    else:
        print("Заметок нет!")
