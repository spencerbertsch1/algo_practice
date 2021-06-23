# Write your MySQL query statement below
-- could use 2 self joins and shift one side down by 1 and then 2 
select distinct l1.num ConsecutiveNums
from Logs l1 
inner join Logs l2 on l1.id = l2.id - 1
inner join Logs l3 on l1.id = l3.id - 2
where l1.num = l2.num and l2.num = l3.num; 
