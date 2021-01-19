# Write your MySQL query statement below
# SELECT Id, Name, Salary, ManagerId

# The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

# +----+-------+--------+-----------+
# | Id | Name  | Salary | ManagerId |
# +----+-------+--------+-----------+
# | 1  | Joe   | 70000  | 3         |
# | 2  | Henry | 80000  | 4         |
# | 3  | Sam   | 60000  | NULL      |
# | 4  | Max   | 90000  | NULL      |
# +----+-------+--------+-----------+


SELECT E1.Name as Employee
FROM
    Employee as E1,
    Employee as E2
WHERE
    E1.ManagerId = E2.Id
    AND
    E1.Salary > E2.Salary


# Here we see a great use case for selecting from the same table twice.
# We can easily solve this problem by calling the same table E1 and E2,
# then applying filtering rules using the 'two' tables.

# This is similar to doing a self join, but more straightforward and in
# this case an easier way to solve the problem.
