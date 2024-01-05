from app import Book, Reader, Review, Annotation

#select books from the year 2020
book_2020 = Book.query.filter(Book.year == 2020).all()
print("All the suggested books in the year 2020:")
[print(book) for book in book_2020]

#instead of all books suggested in 2020, fetch only the first one
book_2020_first = Book.query.filter(Book.year == 2020).first()
print("\nThe first book fetched from the year 2020: ", book_2020_first)

#you can specify multiple criteria for filtering
rev_3_boook13 = Review.query.filter(Review.stars <= 3, Review.book_id == 13).all()
print("\nThe review of 3 stars or lower written for a book with id = 13: ", rev_3_boook13)

#Checkpoint 1: fetching all the readers with "Adams" surname
#adams = 
#[print(person) for person in adams]
adams = Reader.query.filter(Reader.surname == 'Adams').all()
[print(person) for person in adams]

#Checkpoint 2: fetching the first book dating prior to the year 2019
#book_pre2019 = 
#print(book_pre2019)
book_pre2019 = Book.query.filter(Book.year <= 2019).first()
print(book_pre2019)