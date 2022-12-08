#11.1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        print(
            f"The publication for this book is {self.name}. The author is {self.author} and this book has {self.page_count} pages")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_info(self):
        print(f"The publication for this magazine is {self.name}. The chief editor is {self.chief_editor}")


magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Comprament 6", "Rosa Liksom", 192)
magazine.print_info()
book.print_info()
