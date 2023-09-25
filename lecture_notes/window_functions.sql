#Over:
select total_amt_usd, avg(total_amt_usd) OVER (PARTITION BY id)
from orders

#Over with order:
select total_amt_usd, avg(total_amt_usd) 
OVER (PARTITION BY account_id order by occurred_at asc)
from orders

#Rank with Over:
select total_amt_usd,
rank () OVER (PARTITION BY account_id order by account_id asc, total_amt_usd)
from orders

#Dense_Rank:
select total_amt_usd,
rank () OVER (PARTITION BY account_id order by account_id asc, total_amt_usd)
from orders

#Row_Number:
select total_amt_usd,
ROW_NUMBER () OVER (PARTITION BY account_id order by account_id asc, total_amt_usd)
from orders