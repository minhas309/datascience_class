--Question 1
SELECT a.id AS ID, a.name AS Name
FROM  web_events AS w
INNER JOIN accounts AS a
ON a.id = w.account_id AND
w.channel IN ('organic', 'adwords') AND
(DATE_TRUNC('year', w.occurred_at) BETWEEN '2016-01-01' AND '2016-12-31')
GROUP BY a.id, a.name
ORDER BY MAX(w.occurred_at) DESC;

--Question 2
	SELECT r.name AS "region name", sa.name AS "account name",  o.total_amt_usd/ (CASE WHEN o.total = 0 THEN (o.total +0.01)
						  ELSE o.total END) AS "unit Price"
	FROM region AS r
	RIGHT JOIN sales_reps AS sa
	ON r.id = sa.region_id
	LEFT JOIN accounts AS a
	ON sa.id = a.sales_rep_id
	LEFT JOIN orders AS o
	ON a.id = o.account_id

--Question 3
WITH mytable AS (
    SELECT r.name AS "region name", sa.name AS "sales rep name", a.name AS "Account name"
    FROM region AS r
    LEFT JOIN sales_reps AS sa
    ON r.id = sa.region_id
    AND r.name = 'Midwest'
    INNER JOIN accounts AS a
    ON sa.id = a.sales_rep_id
	ORDER BY a.name
)
SELECT * FROM mytable

--Question 4
WITH mytable AS (
    SELECT r.name AS "region name", sa.name AS "sales rep name", a.name AS "Account name"
    FROM region AS r
    LEFT JOIN sales_reps AS sa
    ON r.id = sa.region_id
    AND r.name = 'Midwest'
	AND sa.name LIKE 'S%'
    INNER JOIN accounts AS a
    ON sa.id = a.sales_rep_id
	ORDER BY a.name
)
SELECT * FROM mytable

--Question 5
WITH mytable AS (
    SELECT r.name AS "region name", sa.name AS "sales rep name", a.name AS "Account name"
    FROM region AS r
    LEFT JOIN sales_reps AS sa
    ON r.id = sa.region_id
    AND r.name = 'Midwest'
	AND SUBSTRING(sa.name, POSITION(' ' IN sa.name) + 1) LIKE 'K%'
    INNER JOIN accounts AS a
    ON sa.id = a.sales_rep_id
	ORDER BY a.name
)
SELECT * FROM mytable

--Question 6
SELECT r.name AS "region name", sa.name AS "account name",  o.total_amt_usd/ (CASE WHEN o.total = 0 THEN (o.total +0.01)
					  ELSE o.total END) AS "unit Price"
FROM region AS r
INNER JOIN sales_reps AS sa
ON r.id = sa.region_id
INNER JOIN accounts AS a
ON sa.id = a.sales_rep_id
INNER JOIN orders AS o
ON a.id = o.account_id
AND o.standard_qty > 100

--Question 7 
SELECT r.name AS "region name", sa.name AS "account name",  o.total_amt_usd/ (CASE WHEN o.total = 0 THEN (o.total +0.01)
					  ELSE o.total END) AS "unit Price"
FROM region AS r
INNER JOIN sales_reps AS sa
ON r.id = sa.region_id
INNER JOIN accounts AS a
ON sa.id = a.sales_rep_id
INNER JOIN orders AS o
ON a.id = o.account_id
AND o.standard_qty > 100
AND o.poster_qty > 50

--Question 8
SELECT DISTINCT ac.name,  we.channel
FROM accounts AS ac
INNER JOIN web_events AS we
ON ac.id = we.account_id
AND ac.id = 1001

--Question 9 
SELECT o.occurred_at, a.name AS "account name", o.total AS "order total", o.total_amt_usd AS "order total_amt_usd"
FROM  orders AS o
INNER JOIN accounts AS a
ON a.id = o.account_id AND
(DATE_TRUNC('year', o.occurred_at) BETWEEN '2015-01-01' AND '2015-12-31')

--Question 10
SELECT ac.name AS "account name", we.channel, count(*) AS "# of events"
FROM web_events AS we
INNER JOIN accounts AS ac
ON we.account_id = ac.id
GROUP BY we.account_id, we.channel, ac.name

--Question 11
WITH mytable AS (SELECT sr.name AS "name", we.channel AS "channel", count(*) AS "# of occurrences"
	FROM web_events AS we
	INNER JOIN accounts AS a
	ON a.id = we.account_id
	INNER JOIN sales_reps AS sr
	ON a.sales_rep_id = sr.id
	GROUP BY sr.name, we.channel
	ORDER BY "# of occurrences" DESC
)

SELECT * FROM mytable

--Question 12
--a 
	(SELECT s.name
	FROM accounts AS a
	RIGHT JOIN sales_reps AS s
	ON a.sales_rep_id = s.id
	GROUP BY s.name
	HAVING COUNT(a.*) > 5)
--b
	(SELECT a.name
	FROM accounts AS a
	LEFT JOIN orders AS o
	ON o.account_id = a.id
	GROUP BY a.name
	HAVING COUNT(o.*) = (SELECT MAX(count)
						 FROM(SELECT COUNT(*) AS "count"
							  FROM orders AS o
						 	  GROUP BY o.account_id) AS subquery
						)
	)
--c
	(SELECT a.name
	FROM accounts AS a
	LEFT JOIN orders AS o
	ON o.account_id = a.id
	GROUP BY a.name
	HAVING SUM(o.total_amt_usd) > 30000
	)
--d
	(SELECT a.name
	FROM accounts AS a
	LEFT JOIN orders AS o
	ON o.account_id = a.id
	GROUP BY a.name
	HAVING SUM(o.total_amt_usd) = (SELECT MAX(amount)
								   FROM (SELECT SUM(total_amt_usd) AS amount
										 FROM orders
										 GROUP BY account_id
										) AS subquery
								  )
	)
--e
	(SELECT a.name
	FROM accounts AS a
	LEFT JOIN orders AS o
	ON o.account_id = a.id
	GROUP BY a.name
	HAVING SUM(o.total_amt_usd) = (SELECT MIN(amount)
								   FROM (SELECT SUM(total_amt_usd) AS amount
										 FROM orders
										 GROUP BY account_id
										) AS subquery
								  )
	)
--f
	(SELECT a.name, w.channel
	FROM accounts AS a
	LEFT JOIN web_events AS w
	ON a.id = w.account_id
	AND w.channel = 'facebook'
	GROUP BY a.name, w.channel
	HAVING count(a.*) > 6)
--g
	(SELECT a.name
	FROM accounts AS a
	LEFT JOIN web_events AS w
	ON a.id = w.account_id
	AND w.channel = 'facebook'
	GROUP BY a.name
	HAVING count(a.*) = (SELECT MAX(account)
						 FROM (SELECT COUNT(a.*) AS account
							   FROM accounts AS a
							   LEFT JOIN web_events AS w
							   ON a.id = w.account_id
							   AND w.channel = 'facebook'
							   GROUP BY a.name
						 ) AS subquery
						))

--Question 13
SELECT account_id, total_amt_usd AS "Total amount of order", (CASE WHEN total_amt_usd <= 300 THEN 'Small'
															 WHEN total_amt_usd > 300 AND total_amt_usd < 3000 THEN 'Medium'
															 ELSE 'Large' END) AS "level"
FROM orders

--Question 14
SELECT *, (CASE WHEN total< 1000 THEN 'Less then 1000'
	   WHEN total >= 2000 THEN 'Atleast 2000' 
		ELSE 'Between 1000 and 2000' END) AS "category"
FROM orders

--Question 15
SELECT (CASE WHEN total< 1000 THEN 'Less then 1000'
	   WHEN total >= 2000 THEN 'Atleast 2000' 
		ELSE 'Between 1000 and 2000' END) AS "category", count(*)
FROM orders
GROUP BY (CASE WHEN total< 1000 THEN 'Less then 1000'
	   WHEN total >= 2000 THEN 'Atleast 2000' 
		ELSE 'Between 1000 and 2000' END)
		
--Question 16
SELECT a.name, SUM(o.total_amt_usd) AS "Total Spendings", (CASE WHEN SUM(o.total_amt_usd)< 1000 THEN 'Less then 1000'
	   WHEN SUM(o.total_amt_usd) >= 2000 THEN 'Atleast 2000' 
		ELSE 'Between 1000 and 2000' END) AS "category"
FROM orders AS o
INNER JOIN accounts AS a
ON o.account_id = a.id
AND (DATE_TRUNC('year', o.occurred_at) BETWEEN '2016-01-01' AND '2017-12-31')
GROUP BY a.name
ORDER BY "Total Spendings" DESC

--Question 17
WITH mytable AS (SELECT sr.name, COUNT(o) AS "total orders", (Case
												WHEN COUNT(o) >= 200 THEN 'top'
												ELSE 'not' END) AS "category"
	FROM orders AS o
	INNER JOIN accounts AS a
	ON o.account_id = a.id
	RIGHT JOIN sales_reps AS sr
	ON sr.id = a.sales_rep_id
	GROUP BY sr.name
	ORDER BY category DESC)
	
SELECT * FROM mytable

--Question 18
SELECT DATE_TRUNC('day', occurred_at) AS "Event Day", channel, count(*) AS "# of events"
FROM web_events
GROUP BY DATE_TRUNC('day', occurred_at), channel

--Question 19
SELECT COUNT(o) AS "total orders placed"
FROM orders AS o
INNER JOIN accounts AS a ON o.account_id = a.id
INNER JOIN sales_reps AS sr ON a.sales_rep_id = sr.id
INNER JOIN region AS r ON sr.region_id = r.id
GROUP BY r.name
HAVING SUM(total_amt_usd) = (
    SELECT MAX(total_sales)
    FROM (
        SELECT SUM(total_amt_usd) AS total_sales
        FROM orders AS o
        INNER JOIN accounts AS a ON o.account_id = a.id
        INNER JOIN sales_reps AS sr ON a.sales_rep_id = sr.id
        INNER JOIN region AS r ON sr.region_id = r.id
        GROUP BY r.name
    ) AS subquery
);

--Question 20
WITH temp_tab AS (SELECT r.name, SUM(total_amt_usd) AS total_count, COUNT(o) 
	FROM orders AS o
	INNER JOIN accounts AS a
	ON o.account_id = a.id
	INNER JOIN sales_reps AS sr
	ON a.sales_rep_id = sr.id
	INNER JOIN region as r
	ON sr.region_id = r.id
	GROUP BY r.name
				 )
	
SELECT count AS "total orders placed"
FROM temp_tab 
WHERE total_count = (SELECT MAX(total_count) FROM temp_tab);