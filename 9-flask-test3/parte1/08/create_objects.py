#This is a separate Python script in which we practice creating database objects
#You can also perform these operations in command-line terminal
from app import Reader, Book, Review

b1 = Book(id = 123, title = 'Demian', author_name = "Hermann", author_surname = 'Hesse', month = "February", year = 2020)
r1 = Reader(id = 342, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')

print("My first reader:", r1.name)

#Checkpoint 1: 
b2 = Book(id = 533, title = 'The Stranger', author_name = "Albert", author_surname = 'Camus', month = "April", year = 2019)
#Checkpoint 2: 
r2 = Reader(id = 765, name = 'Sam', surname = 'Adams', email = 'sam.adams@example.com')
#Checkpoint 3: 
print(b2.author_surname)
#Checkpoint 4:
print(len(r2.email))
