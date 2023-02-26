class Label:
    def __init__(self, title, text, idTemp):
        self.id = idTemp
        self.title = title
        self.text = text

    def info(self):
        return "id: {}\nTitle:{}\n {}".format(self.id, self.title, self.text)
