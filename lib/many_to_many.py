class Author:
    all_authors = []

    def __init__(self, name):# module Test Author class initializes with name
        self.name = name
        self.all_contracts = []
        Author.all_authors.append(self)

    def contracts(self):# module Test Author class has method contracts() that returns a list of its contracts
        return self.all_contracts

    def books(self):# module Test Author class has method books() that returns a list of its books
        return [contract.book for contract in self.all_contracts]

    def sign_contract(self, book, date, royalties):# module Test Author class has method sign_contract() that creates a contract for an author and book
        contract = Contract(self, book, date, royalties)
        self.all_contracts.append(contract)
        return contract

    def total_royalties(self):# module Test Author class has method total_royalties that gets the sum of all its related contracts' royalties
        return sum(contract.royalties for contract in self.all_contracts)


class Book:
    all_books = []

    def __init__(self, title):# module Test Book class initializes with title
        self.title = title
        self.all_contracts = []
        Book.all_books.append(self)

    def contracts(self):# module Test Book class has method contracts() that returns a list of its contracts
        return self.all_contracts

    def authors(self):# module Test Book class has method authors() that returns a list of its authors
        return [contract.author for contract in self.all_contracts]


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):# Contract  initializes with author, book, date, royalties
        self.validate_author(author)# module Test Contract class validates author of type Author 
        self.validate_book(book)# module Test Contract class validates book of type Book 
        self.validate_date(date)# module Test Contract class validates date of type str 
        self.validate_royalties(royalties)# module Test Contract class validates royalties of type int 

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        author.all_contracts.append(self)
        book.all_contracts.append(self)
        Contract.all_contracts.append(self)

    @staticmethod
    def validate_author(author):# module Test Contract class validates author of type Author 
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")

    @staticmethod
    def validate_book(book):# module Test Contract class validates book of type Book 
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        

#FAILED module Test Contract class has method contracts_by_date() that sorts all contracts by date - assert [<many_to_man...d4f0190>, ...] == [<many_to_man...75c05d4e7070>]
#================================================ 1 failed, 13 passed in 0.20s ================================================

    @staticmethod
    def validate_date(date):# module Test Contract class validates date of type str 
        if not isinstance(date, str):
            raise TypeError("Date must be a string")

    @staticmethod
    def validate_royalties(royalties):# module Test Contract class validates royalties of type int 
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")

    @classmethod
    def contracts_by_date(cls, date):# module Test Contract class has method contracts_by_date() that sorts all contracts by date 
        return [contract for contract in cls.all_contracts if contract.date == date]
    

