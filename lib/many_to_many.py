class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    def contracts(self):
         return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return [contract.book for contract in self.contracts()]
    def sign_contract(self,book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    

class Book:

    all = []

    def __init__(self, title): 
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod  
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

# all properties for the Contract class
    
    @property
    def author(self):
        return self._author 
    
    @property
    def book (self):
        return self._book
    
    @property
    def date(self):
        return self._date
    
    @property
    def royalties(self):
        return self._royalties
    
# all property setters for the Contract class
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @book.setter
    def book(self,value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    @date.setter
    def date(self,value):
        if not isinstance(value, str):
            raise Exception
        self._date = value
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value

    
