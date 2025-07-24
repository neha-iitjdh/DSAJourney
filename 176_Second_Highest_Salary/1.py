select (select distinct(salary) from Employee
order by salary desc limit 1 offset 1) as SecondHighestSalary

#This is a sql command but I am storing it in py file