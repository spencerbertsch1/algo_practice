# Write your MySQL query statement below

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id is the primary key for this table.
# This table contains information about the temperature in a certain day.

# Write an SQL query to find all dates' id with higher temperature compared
# to its previous dates (yesterday).

# Return the result table in any order.

# we only select the ID column
SELECT t1.Id

# here we use an inner self join
FROM Weather t1
INNER JOIN Weather t2

# we want to do the join such that each record in t1
# joins with the following date in t2
# ON t1.id - 1 = t2.id
ON TO_DAYS(t1.recordDate) = TO_DAYS(t2.recordDate) + 1

# lastly we do the check to see if t2's day was hotter
WHERE t1.Temperature > t2.Temperature

# And here we see one of the useful uses for self joins!
# we can do an inner self join on an 'ID' column and we
# can easily shift one of the columns by one.

# This let's us easily create an lagging or leading column
# which we can use to limit a result set or generate a new,
# derived feature.