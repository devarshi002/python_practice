class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_description(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    

#usage
book1 = Book("To kill a Mockingbird", "harper lee", 1960)
print(book1.get_description())