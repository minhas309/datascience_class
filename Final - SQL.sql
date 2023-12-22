select id, name, website, lat, long, primary_poc, sales_rep_id
from accounts

select id, account_id, occurred_at, standard_qty, gloss_qty, poster_qty, total, standard_amt_usd, gloss_amt_usd, poster_amt_usd, total_amt_usd
from orders

select id, name
from region

select id, name, region_id
from sales_reps

select id, account_id, occurred_at, channel
from web_events


--Difficult Filtering Questions:
--Q1
select *
from accounts as a join sales_reps as s on a.sales_rep_id = s.id join region as r on s.region_id = r.id
where r.name = 'Southeast' and a.website like '%face%' and a.primary_poc is not NULL;

--Q2
select *
from orders
where (occurred_at between '2015-01-01' and '2015-06-30') and total_amt_usd > 5000;

--Q3
select *
from accounts
where id in (select account_id
			from orders
			where total > (select avg(total)
						   from orders))

--Q4
select a.name, w.occurred_at, w.channel
from accounts as a join web_events as w on a.id = w.account_id join sales_reps as s on a.sales_rep_id = s.id join region as r on s.region_id = r.id
where r.name = 'Northeast' and w.channel = 'facebook';

--Q5
select *
from accounts
where (name like 'a%' or name like 'e%' or name like 'i%' or name like 'o%' or name like 'u%') and primary_poc like '%Mac%'

--Q6
select *
from sales_reps as s join region as r on s.region_id = r.id join accounts as a on a.sales_rep_id = s.id join orders as o on o.account_id = a.id
where r.name = 'West' and o.total > (select avg(total)
						   from orders)
						   
						   
--Data Sorting
--Q1
select o.*, a.name as account_name, s.name as sales_representative_name
from orders as o join accounts as a on o.account_id = a.id join sales_reps as s on a.sales_rep_id = s.id
order by occurred_at desc
limit 10;


--Join & Filter
--Q1
select a.name, o.standard_qty
from orders as o join accounts as a on o.account_id = a.id
where o.total > (select avg(total)
			  from orders)
			  
			  
--Aggregation Functions
--Q1
select s.name, 
	   count(a.id) as number_of_account_manage, 
	   min(o.total) as minimum_total_quantity, 
	   max(o.total) as maximum_total_quantity, 
	   avg(o.total) as average_total_quantity, 
	   sum(o.total_amt_usd) as total_amount_in_usd, 
	   case when avg(o.total) > 500 then 'High'
			when avg(o.total) between 200 and 500 then 'Medium'
			when avg(o.total) < 200 then 'Low'
		end as High_or_low
from accounts as a join sales_reps as s on a.sales_rep_id = s.id 
join orders as o on o.account_id = a.id
where s.name like '%w%' and 
	 (o.occurred_at between '2015-01-01' and '2015-12-31') and 
	 EXISTS(select account_id
			from orders
			where account_id = account_id)
group by s.name
order by number_of_account_manage desc
limit 10


--SubQueries
--Q1
select a.name as "account name",
	   count(o.id) as numbers_of_orders, 
	   avg(o.total) as "average_total_orders",
	   s.name as "sales representative name",
	   case when avg(o.total) > 500 then 'High'
			when avg(o.total) between 200 and 500 then 'Medium'
			when avg(o.total) < 200 then 'Low'
		end as High_or_low
from accounts as a join orders as o on a.id = o.account_id
	 left join sales_reps as s on a.sales_rep_id = s.id 
where o.total > (select avg(total)
				from orders) and Exists(select account_id
									   from orders as o2
									   where o2.account_id = a.id) and o.total_amt_usd = (select max(total_amt_usd)
																				 		  from orders) 
group by a.name, s.name
having avg(o.total) > (select avg(total) from orders);


--Windows Function
--Q1
WITH 
  rank_func AS (
    SELECT 
      o.id,
      a.name, 
      o.total,
      RANK() OVER (PARTITION BY o.total ORDER BY o.total DESC) AS "Rank"
    FROM 
      accounts AS a
      JOIN orders AS o ON a.id = o.account_id
  ),
  
  dense_func AS (
    SELECT 
      o.id,
      a.name, 
      o.total,
      DENSE_RANK() OVER (PARTITION BY a.name ORDER BY o.total_amt_usd ASC) AS "Dense_Rank"
    FROM 
      accounts AS a
      JOIN orders AS o ON a.id = o.account_id
  ),
  
  sum_func AS (
    SELECT 
      o.id,
      a.name, 
      o.total,
      SUM(o.total) OVER (PARTITION BY a.name ORDER BY o.id) AS "Sum"
    FROM 
      accounts AS a
      JOIN orders AS o ON a.id = o.account_id
  ),
  
  avg_func AS (
    SELECT 
      o.id,
      a.name, 
      o.total,
      AVG(o.total_amt_usd) OVER (PARTITION BY a.name ORDER BY o.occurred_at) AS "Average"
    FROM 
      accounts AS a
      JOIN orders AS o ON a.id = o.account_id
  ),
  
  row_func AS (
    SELECT 
      o.id,
      a.name, 
      o.total,
      ROW_NUMBER() OVER (PARTITION BY a.name ORDER BY o.total DESC) AS "Top 3"
    FROM 
      accounts AS a
      JOIN orders AS o ON a.id = o.account_id
  )
  
SELECT * FROM dense_func


--Data Cleaning Functions
--Q1
select concat(Substring(primary_poc from 1 for position(' ' in primary_poc)-1),
			  '.',
			  Substring(primary_poc from position(' ' in primary_poc)+1),
			  '@',
			  lower(replace(name,' ','')),'.com') as email,
	   concat(lower(left(primary_poc,1)),lower(substring(primary_poc from position(' ' in primary_poc)+1 for 1)),
			  lower(substring(primary_poc from position(' ' in primary_poc)-1 for 1)),
			  lower(right(primary_poc,1)),
			  replace(lower(substring(name from (length(name)/2)-2 for (length(name)/2)+2)),' ','')) as password
from accounts





















