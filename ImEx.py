import csv
from label import *


def importNote():
    notes = []
    with open('Notes.csv', 'r')as f:
        book = csv.reader(f, delimiter=";")
        for n in book:
            note = Label(n[0], n[1], n[2], n[3])
            notes.append(note)
    print("Импорт завершен!")
    return notes


def exportNote(notes):
    if (len(notes) > 0):
        with open('Notes.csv', 'w') as f:
            exp = csv.writer(f, delimiter=";", lineterminator="\r")
            for x in notes:
                exp.writerow([x.title, x.text, x.date, x.id])
        print("Экспорт выполнен!")
    else:
        print("Нет элементов для экспорта!")
