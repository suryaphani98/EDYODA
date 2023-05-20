/* 1. Count the number of Salesperson whose name begin with ‘a’/’A’*/                                  

select * from SalesPeople where Sname like 'A%' or 'a%';

/* 2. Display all the Salesperson whose all orders worth is more than Rs. 2000.*/

select Sname,s.Snum,Amt from salespeople s join orders o on s.Snum = o.Snum 
where Amt > 2000;

/* 3. Count the number of Salesperson belonging to Newyork.*/

select count(*) from SalesPeople where city = 'Newyork';

/* 4. Display the number of Salespeople belonging to London and belonging to Paris.*/ 

select * from salespeople where city in ('London','Paris');

/*5. Display the number of orders taken by each Salesperson and their date of orders.*/

select s.Sname,count(*) as orders_count from orders o join salespeople s on s.Snum = o.Snum
group by o.Snum;

















