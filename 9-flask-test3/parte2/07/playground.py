from app import db, Book, Reader #notice we import db here as well
import add_data

#fetch the reader with id = 123 and change their e-mail
reader = Reader.query.get(123)
print("Before the change:", reader) #print before the change
reader.email = "new.email@example.com"
db.session.commit()
print("After the commit:", Reader.query.get(123)) #print after the change

#rollback
reader = Reader.query.get(345)
print("Rollback example - before the change: ", reader) #print before the change
reader.email = "new.email@example.edu"
db.session.rollback()
print("Rollback example - after the rollback: ", Reader.query.get(345)) #print after the change

print("\nCheckpoint 1: use get to fetch a book entry:")
#book_19 = 
book_19 = Book.query.get(19)
print("\nCheckpoint 2: modify the month attribute to June:")
#your code here
book_19.month = "June"
print("\nCommit the change:")
#your code here
db.session.commit()

