# Polymorphism with inheritance

class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        print("This is general Document section: ", self.title)


class PDFDocument(Document):
    def __init__(self, title):
        super().__init__(title)

    def describe(self):
        print("This is Pdf Document section: ", self.title)


class TextDocument(Document):
    def __init__(self, title):
        super().__init__(title)

    def describe(self):
        print("This is Text Document section: ", self.title)


documents = [
    PDFDocument("Sales Report 2026"),
    TextDocument("Student Mark Sheet"),
    PDFDocument("2027 Calender Events"),
    TextDocument("Weather Forecast report"),
    TextDocument("Global Warming Report 2025")
]

for document in documents:
    document.describe()
