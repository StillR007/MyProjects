use billing_simple;

INSERT INTO billing (
payer_email, recipient_email, sum, currency, billing_date, comment) VALUES (
'alex@mail.com', 'leo@mail.com', '500.00', 'MYR', '2010-08-20', 'Here are some money for you');

select * from billing where comment = 'Here are some money for you';

update billing set currency = 'EUR' where billing_date='2010-08-20' and comment = 'Here are some money for you';

update billing set payer_email = 'igor@mail.com' where payer_email='alex@mail.com';

delete from billing WHERE comment = 'Here are some money for you';

DELETE FROM billing WHERE 
payer_email is NULL OR recipient_email = ''
AND payer_email = '' OR recipient_email is NULL;

select * from billing;