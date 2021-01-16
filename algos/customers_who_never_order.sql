/* 183. Customers Who Never Order */

SELECT Name as Customers
FROM Customers
WHERE Customers.id NOT IN (
    SELECT CustomerId
    FROM Orders
);