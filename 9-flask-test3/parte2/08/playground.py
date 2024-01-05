from app import db, Book, Reader, Review #notice we import db here as well

#let us first print all the readers current in the database (image on the right)
for reader in Reader.query.all():
   print(reader)

#print all the reviews
print("\nAll the current reviews:")
for review in Review.query.all():
  print(review)  

#delete reader with id = 753 (Nova Yeni, nova.yeni@example.com)
db.session.delete(Reader.query.get(753))

#print readers again to validate that the reader is indeed deleted
print("\nReaders after deleting a rader with id = 753")
for reader in Reader.query.all():
   print(reader)

#print reviews to see that all the reviews made by reader id = 753 are deleted
#(see the image on the right)
#print all the reviews
print("\nAll the current reviews:")
for review in Review.query.all():
  print(review)  

#Checkpoint 1:
#your code here below
db.session.delete(Reader.query.get(123))


