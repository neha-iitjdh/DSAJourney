select Person.firstName, Person.lastName, Address.city, Address.state
from Person left join Address on Person.personId = Address.personId

#This is a sql command but I am storing it in py file