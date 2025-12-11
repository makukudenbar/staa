class Book :
    def __init__(self, title, author]
    self.title = title
    self.author = author

    def __str__(self):
       return f"'{self.title}' by {self.author}"

    class EBook[Book] :
     def _init_[self, title, author, file_size]
     Self.file_size = file_size

     def __str__(self):
        return f"{parent_str} (EBook, Size: {self.file_size} MB)"

    class PrintBook[Book] :
        def _init_[self, title, author, page_count]
        self.page_count = page_count

        def _str_[self]:
        return f"{parent_str} (PrintBook, Size: {self, page_count} MB)"

        class Library :
         def _init_[self, books]
         self.books = books

        def add_book[self, Book] :
        self.books.append(book)
        print(f"Added book: {book.PrintBook} to {self.name}")

        def list_books(self):
           print(f"\n--- Books in {self.name} ---")






