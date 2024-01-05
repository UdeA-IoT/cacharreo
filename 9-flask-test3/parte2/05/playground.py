from app import db, Book, Reader, Review

#retrieve all reader with .edu e-mails
education = Reader.query.filter(Reader.email.endswith('edu')).all()
print(education)

#retrieve all readers with e-mails that contain a . before the @ symbol
emails = Reader.query.filter(Reader.email.like('%.%@%')).all()
print("\nReaders with e-mails having a . before the @ symbol:")
for e in emails:
  print(e.email)

#order all books by year
ordered_books = Book.query.order_by(Book.year).all()
print("\nBooks ordered by year:")
for book in ordered_books:
  print(book.title, book.year)

print("\nCheckpoint 1: your code here below:")
#s_names = 
#print(s_names)
s_names = Reader.query.filter(Reader.surname.endswith('s')).all()
print(s_names)

print("\nCheckpoint 2: your code here below:")
#sample_emails = 
#print(sample_emails)
sample_emails = Reader.query.filter(Reader.email.like('%@sample%')).all()
print(sample_emails)

print("\nCheckpoint 3: your code here below:")
#ordered_reviews = 
#print(ordered_reviews)
ordered_reviews = Review.query.order_by(Review.stars).all()
print(ordered_reviews)