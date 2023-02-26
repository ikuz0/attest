from label import *
import datetime


def addNote(notes):
    noteTemp = inputNote(notes)
    return Label(noteTemp[0], noteTemp[1], noteTemp[2], noteTemp[3])


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
