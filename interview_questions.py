# Implement a class representing Book. Create the constructor.
# Write a method to determine if 2 instances of Book are the same
# Write a method to compare 2 libraries and determine if they are the same
    # takes 2 lists of books; assume libraries don't have duplicate books,
    # books in libraries can be in any order

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    def __eq__(self, other_book):
        return self.title == other_book.title and \
            self.author == other_book.author and \
            self.genre == other_book.genre

def are_libraries_equivalent(library1, library2):
    library1.sort()
    library2.sort()
    print(library1 == library2)

harry_potter = Book("Harry Potter", "J.K. Rowling", "YA")
the_cruel_prince = Book("The Cruel Prince", "Holly Black", "YA")
print(harry_potter == the_cruel_prince)
print(harry_potter == harry_potter)