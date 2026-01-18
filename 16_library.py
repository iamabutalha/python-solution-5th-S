class Library:
    def __init__(self):
        self.books  = {}
    
    def add_book(self, title, author):
        if title in self.books:
            print("Book Already exist")
        else:
            self.books[title] = {'author': author, 'title': title, 'status': "Avaliable"}
            print("Book added successfully")
    
    def remove_book(self, title):
        if title not in self.books:
            print("Book Not found")
        else:
            del self.books[title]
            print("Book removed successfully")
    
    def search_book(self, query):
        found = False

        for title, book in self.books.items():
            if query.lower() in title.lower() or query.lower in book['author'].lower():
                print(f"Title: {title}, Book Name: {book}, status {book['status']}")
                found = True


lib = Library()
lib.add_book("The hard", "DES")
lib.search_book("The hard")