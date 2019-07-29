import person
import shelve


bob = person.Person("bob")
sue = person.Manager('susan', 1000)

# shelve允许按键存储pickle处理后的对象，
db = shelve.open('persondb')
for object in (bob, sue):
    db[object.name] = object # 把对象的名字做键，赋给shelve
db.close()

new_db = shelve.open('persondb')
for db in new_db:
    print(new_db[db])
new_db.close()