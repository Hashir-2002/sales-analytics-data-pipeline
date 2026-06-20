-- Total revenue
SELECT SUM(Orders.quantity * Products.price) AS total_revenue
FROM Orders
JOIN Products ON Orders.product_id = Products.product_id;


-- Revenue per product
SELECT Products.product_name,
       SUM(Orders.quantity * Products.price) AS revenue
FROM Orders
JOIN Products ON Orders.product_id = Products.product_id
GROUP BY Products.product_name;

-- Top customer
select TOP 1 
    Customers.name, Orders.customer_id,sum(Orders.quantity*Products.price) as revenue_per_customer from Orders INNER JOIN Products on Orders.product_id=Products.product_id 
        INNER JOIN Customers ON Orders.customer_id=Customers.customer_id group by Customers.name,Orders.customer_id order by revenue_per_customer DESC


-- Most expensive product ordered by each customer --

select Customers.name as Customer_Name ,Products.price,Products.product_name from Orders 
    Inner join Products on Products.product_id=Orders.product_id
    Inner join Customers on Customers.customer_id=Orders.customer_id WHERE Products.price = (
    SELECT MAX(Products.price)
    FROM Orders o2
    INNER JOIN Products ON Products.product_id = o2.product_id
    WHERE o2.customer_id = Orders.customer_id
)
    order by Customers.customer_id 


    --Revenue by each customer--


select Customers.name,  sum(Orders.quantity*Products.price) AS REVENUE_PER_CUSTOMER FROM PRODUCTS INNER JOIN Orders
ON Orders.product_id=Products.product_id
INNER JOIN Customers on  Customers.customer_id=Orders.customer_id 
GROUP BY  Customers.name ORDER BY REVENUE_PER_CUSTOMER DESC
 