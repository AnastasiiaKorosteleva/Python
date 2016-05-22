import sqlite3 as sql


query = "select Users.name, Orders.id, sum(price) from Users " \
        "inner join Orders on Users.id = user_id " \
        "inner join GoodsInOrders on Orders.id = order_id " \
        "inner join Goods on Goods.id = good_id " \
        "where paid = 0 and Users.id = ? " \
        "group by Orders.id"


def unpaid(user_id):
    with sql.connect("data.sqlite") as table:
        cur = table.cursor()
        x = cur.execute(query, [user_id]).fetchall()

    return x

print(unpaid(23))

#[('Maria Doomhammer', 58, 45013.15), ('Maria Doomhammer', 374, 5110.61), ('Maria Doomhammer', 1039, 4.84)]
