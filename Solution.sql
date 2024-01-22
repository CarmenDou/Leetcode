select *
from Accounts
where id in (
select distinct id
from (
select id,ROW_NUMBER() OVER(PARTITION BY id ORDER BY login_date) as ranking, login_date
from (
select distinct id,login_date
from logins
) X
) X
group by id,date_add(login_date, interval -ranking day)
having count(*) >= 5
)



