from app import db, Reader #notice we import db here as well
import add_data #we use this script to recreate the database, put all the entries so every time you run this script
                #you get the same result

#creating new readers
new_reader1 = Reader(name = "Nova", surname = "Yeni", email = "nova.yeni@sample.com")
new_reader2 = Reader(name = "Nova", surname = "Yuni", email = "nova.yeni@sample.com")
new_reader3 = Reader(name = "Tom", surname = "Grey", email = "tom.grey@example.edu")

print("Before addition: ")
for reader in Reader.query.all():
  print(reader.id, reader.email)

print("\nNote that before committing, the id of the new readers is: ", new_reader1.id, "\n")

#adding the first reader - the commit should succeed
db.session.add(new_reader1)
try:
    db.session.commit()
    print("Commit succeded.", new_reader1, "added to the database permanently. The exception was not raised.\n")
except:
    db.session.rollback()

#adding the second reader - the commit should fail because e-mails should be unique
db.session.add(new_reader2)  
try:
    db.session.commit()
except Exception as ex:
    print("The commit of", new_reader2,"didn't succeed. Duplicate primary key values. We will empty the current session.\n")
    print("The error is the following:", ex)
    db.session.rollback() 

#adding the third reader - the commit should succeed
db.session.add(new_reader3)  
try:
    db.session.commit()
    print("Commit succeded.", new_reader3, "added to the database permanently. The exception was not raised.\n")
except Exception as ex:
    db.session.rollback() 

print("\nNote that after committing, the id of the new readers is now: ", new_reader1.id, "\n")

#print all the readers after the addition, and we see nova.yeni@sample.com there, but not twice
for reader in Reader.query.all():
  print(reader.id, reader.email)
print("\nThe new readers Nova Yeni and Tom Grey are in the database. Notice that Nova Yeni doesn't appear twice.\n")

print("\nCheckpoint 1: create a new_reader:")
#new_reader = 
new_reader = Reader(name = "Peter", surname = "Johnson", email = "peter.johnson@example.com")
print("\nCheckpoint 2: add the new reader to the database:")
#your code here
db.session.add(new_reader)
print("\nCheckpoint 3: commit and rollback if exception is raised:")
try:
  db.session.commit()
except:
  db.session.rollback()
