class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_info(self):
        return f"Judul: {self.title}, Penulis: {self.author}, Tahun: {self.year}"


# Membuat objek Book
book = Book("Purple Cow", "Seth Godin", 2002)

# Memanggil method get_book_info
print(book.get_book_info())