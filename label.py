class Label:
    def __init__(self, title, text, date, idTemp):
        self.id = idTemp
        self.title = title
        self.date = date
        self.text = text

    def info(self):
        return "id: {}\nЗаголовок: {}\nТекст: {}\nСоздана: {}".format(self.id, self.title, self.text, self.date)
