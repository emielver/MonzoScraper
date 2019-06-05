class Post:
    
    def __init__(self, author, position, title, date, text):
        self.author = author
        self.position = position
        self.title = title
        self.date = date
        self.text = text

    def get_author(self):
        return self.author

    def get_position(self):
        return self.position
    
    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def get_text(self):
        return self.text
