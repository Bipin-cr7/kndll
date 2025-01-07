'''
Task: Create a simple Book class that has the following attributes: title, author, and year_published.
 It should also have a method display_info() that prints the book’s details.
Skills to Practice: Classes, objects, constructors, and methods.
'''
class Book:
    def __init__(self ,tittle,author,year_published):
        self.tittle= tittle
        self.author= author
        self.year_published=year_published

    def display_info(self):
        print(f"Book {self.tittle} was written by {self.author} in year {self.year_published} ")

Book1=Book("Secret","DR.Nicole Ivanov", "1923")
Book1.display_info()
   