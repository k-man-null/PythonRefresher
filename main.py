from Person import People
from Student import Student

alice = People("Alice", 10, "01/01/2000", "12345678", "alice@gmail.com")
bob = People("Bob", 20, "20/04/1999", "44449999", "bob@gmail.com")
carl = People("Carl", 30, "10/10/2010", "12341234", "carl@gmail")

persons = [alice, bob]
persons.append(carl)

print(alice.getAge())