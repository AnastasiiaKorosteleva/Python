__author__ = 'anastasiiakorosteleva'

import heapq, random
import sqlite3 as sq

with sq.connect("data.sqlite") as con:
    cur = con.cursor()
#1
    for row in cur.execute(
            "select * from Users; "):
        print(row)
#2
    for row in cur.execute(
            "select count(Users.id) from Users "):

        print(row)
#3
    for row in cur.execute(
            "select count(Users.id) from Users where birth_date >= date('1976-05-11') "):

        print(row)
#4
    for row in cur.execute(
            "select Users.country, count(Users.country) "
            "from Users "
            "group by Users.country "):
        print(row)
#5
    for row in cur.execute(
            "select Users.name, count(Users.name) "
            "from Users "
            "group by Users.name "
            "having count(Users.name) != 1 "):

        print(row)
#6
    for row in cur.execute(
            "select count(Orders.id) from Orders "):
            print(row)

#7(все максимумы)
    for row in cur.execute(
            "select Orders.created, count(Orders.created) "
            "from Orders "
            "group by date(Orders.created) "
            "having count(Orders.created) = 4 "):

        print(row)
#
# #7_1(один из максимумов -- первый)
    for row in cur.execute(
            "select date(created), count(*) as num "
            "from Orders "
            "group by date(Orders.created) "
            "order by num desc limit 1 "):

        print(row)
#8

    for row in cur.execute(
            "select 100 - sum(paid) * 100.0 / count(*) "
            "from Orders "
            ):

        print(row)
#9

    for row in cur.execute(
        "select * from Goods "
        "where name like '%bread%'" ):

        print(row)

#10
    for row in cur.execute(

        "select id, name, count(*) as num "
        "from GoodsInOrders "
        "inner join Goods on id = good_id "
        "group by GoodsInOrders.good_id "
        "order by num desc limit 10 "):
        print(row)
#11

    for row in cur.execute(
        "select sum(price) "
        "from Goods "
        "inner join GoodsInOrders "
        "on Goods.id = good_id "
        "inner join Orders "
        "on Orders.id = order_id "
        "where paid = 1 "
    ):
        print(row)

#12
    for row in cur.execute(
        "select Goods.id, Goods.name "
        "from Goods "
        "inner join GoodsInOrders "
        "on Goods.id = good_id "
        "inner join Orders "
        "on order_id = Orders.id "
        "inner join Users "
        "on Users.id = user_id "
        "where gender = 'F' "
        "group by Goods.name "
        "order by count(*) desc limit 10 "):
        print(row)




#13
    for row in cur.execute(
         "select Users.id, Users.name from Users "
         "inner join Orders on Users.id = user_id "
         "inner join GoodsInOrders on Orders.id = order_id "
         "inner join Goods on Goods.id = good_id "
         "where units = 'KG' "
         "group by user_id "
         "order by sum(quantity) desc limit 1 "):
        print(row)