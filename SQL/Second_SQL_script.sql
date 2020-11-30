use project_simple;

select avg(budget) from project;

select count(*) from project;

update project SET project_finish=null where project_finish < project_start;

select project_finish, project_start,
datediff(project_finish, project_start) from project where project_finish is not null;

select 
	AVG(datediff(project_finish, project_start)), 
    max(datediff(project_finish, project_start)),
    min(datediff(project_finish, project_start))
from project where project_finish is not null;

select 
	AVG(datediff(project_finish, project_start)) as avg_days, 
    max(datediff(project_finish, project_start)) as max_days,
    min(datediff(project_finish, project_start)) as min_days,
    client_name
from project where project_finish is not null
group by client_name
order by max_days desc
limit 10;

