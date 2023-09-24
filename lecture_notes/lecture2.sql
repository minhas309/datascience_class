SELECT CONCAT('Abdullah', 'Minhas') AS concat, ('Abdullah' || 'Minhas') AS pipe;

SELECT RIGHT(website, 3) AS website, COUNT(*)
FROM accounts
GROUP BY 1;

SELECT POSITION('.' IN RIGHT(website, -4)) +4, website
FROM accounts;

SELECT POSITION('.' IN RIGHT(website, -4)) +4, LENGTH(website)
FROM accounts;

SELECT POSITION('.' IN RIGHT(website, -4)) +4, UPPER(website)
FROM accounts;

SELECT POSITION('.' IN RIGHT(website, -4)) +4, SUBSTRING(website from 5)
FROM accounts;

SELECT SUBSTRING((occurred_at::VARCHAR) FROM 1 FOR 4) AS year, SUBSTRING((occurred_at::VARCHAR) FROM 9 FOR 2) AS day, occurred_at
FROM web_events;

-- SELECT CONCAT(FName, ',' , LName,'@',name,'.com' ) AS email
-- FROM accounts,
--  	(SELECT (SUBSTRING(primary_poc FROM 1 FOR (POSITION (' ' IN primary_poc))))
-- 		FROM accounts) AS FName,
-- 		(
-- 		SELECT (SUBSTRING(primary_poc FROM (POSITION (' ' IN primary_poc)) ))
-- 		FROM accounts) AS LName
-- ;

SELECT LOWER(CONCAT((SUBSTRING(primary_poc FROM 1 FOR (POSITION (' ' IN primary_poc))-1)), ',' , (SUBSTRING(primary_poc FROM (POSITION (' ' IN primary_poc))+1 )),'@',name,'.com' )) AS email,
CONCAT(LEFT((SUBSTRING(primary_poc FROM 1 FOR (POSITION (' ' IN primary_poc)))),1), LEFT((SUBSTRING(primary_poc FROM (POSITION (' ' IN primary_poc))+1 )),1), 
RIGHT(RIGHT((SUBSTRING(primary_poc FROM 1 FOR (POSITION (' ' IN primary_poc))-1)),1),1),RIGHT((SUBSTRING(primary_poc FROM (POSITION (' ' IN primary_poc))+1 )),1),'@',SUBSTRING(name FROM 1 FOR 3)
	  ) AS password
FROM accounts;

SELECT o.id, a.primary_poc, COALESCE(a.primary_poc, 'no poc')
FROM orders o
LEFT JOIN accounts a
ON o.account_id = a.id
AND standard_qty IS NULL