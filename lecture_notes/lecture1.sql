SELECT * FROM accounts WHERE id>1001 LIMIT 10
id account name, sales, name
Accounts and sales_ref

SELECT * FROM accounts AS a JOIN sales_rep_id AS s ON a.sales_ref_id = s.id

SELECT * FROM accounts AS a JOIN sales_rep_id AS s ON a.sales_ref_id = s.id

name, person of contact, channle_info

SELECT a.name, FROM accounts AS a JOIN web_events AS we ON a.id = we.account_id WHERE a.website = 'Walmart'

SELECT Count(*) FROM
{SELECT a.name, FROM accounts AS a JOIN web_events AS we ON a.id = we.account_id WHERE a.website = 'Walmart'} AS tab1

SELECT a.name, FROM accounts AS a JOIN web_events AS we ON a.id = we.account_id WHERE a.website = 'Walmart' AND (DATE_TRUNC('year', we.occured_at) BETWEEN '2016-01-01' AND '2016-12-31')