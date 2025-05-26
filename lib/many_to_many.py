from datetime import datetime

class Author:
    all_authors = []
    def __init__(self, name):
        self.name = name
        self._book = None #if no value is assigned
        Author.all_authors.append(self)

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Value must be an instance of Book")
    
    def contracts(self):
        return [c for c in Contract.all if c.author == self]
    
    def books(self):
        return [b.book for b in Contract.all if b.author == self]
    
    def sign_contract(self, book, date, royalties):
        if isinstance(book, Book):
            return Contract(self, book, date, royalties)
        else:
            raise Exception('book must be an instance of Book')

    def total_royalties(self):
        royalties = [r.royalties for r in Contract.all if r.author == self]
        return sum(royalties)
        


class Book:
    all_books = []
    def __init__(self, title):
        self.title = title
        self._author = None
        Book.all_books.append(self)


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, author):
            self._author = author
        else:
            raise Exception("Value must be an instance of Book")
    
    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return [a.author for a in Contract.all if a.book == self]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book) and isinstance(date, str) and isinstance(royalties, int):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            Contract.all.append(self)
        else:
            raise Exception('Values must be instances of Book and Author, and date must be a string, while royalties must be an integer')
        
    
    @classmethod
    def contracts_by_date(cls, date_string):
        cls.all.sort(key=lambda item: datetime.strptime(item.date, '%m/%d/%Y'))
        return [contract for contract in cls.all if contract.date == date_string]