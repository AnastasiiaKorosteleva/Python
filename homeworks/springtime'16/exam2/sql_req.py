__author__ = 'anastasiiakorosteleva'

import sqlite3 as sq

with sq.connect("control.sqlite") as con:
    cur = con.cursor()
#1
    # for row in cur.execute(
    #         "select * from Users order by Users.username asc "):
    #     print(row)

# #2
#     for row in cur.execute(
#             "select Users.username "
#             "from Users "
#             "order by Users.registered asc limit 5 "):
#         print(row)
#3

    # for row in cur.execute(
    #     "select username, user_id, count(*) as num "
    #     "from listened "
    #     "inner join users on users.id = user_id "
    #     "group by user_id "
    #     "order by num desc limit 5; "):
    #     print(row)

#4

# for row in cur.execute(
#
#         "select Artists.name, count(Albums.name) as num "
#         "from Artists "
#         "inner join Albums on Artists.id = artist_id "
#         "group by Artists.name "):
#         # "order by num desc limit 10 "):
#     print(row)
# #

#5-?

    # for roe in cur.execute(
    #     "select Artists.name, count(*) as num "
    #     "from Artists "
    #     "inner join Albums on Artists.id = Albums.artist_id "
    #     "inner join Songs on Songs.album_id = Albums.id "
    #     "group by Artists.id order by num desc limit 1 "):
    #     print(roe)

#6(+TINA_PACKER!!!)

    # for row in cur.execute(
    #     "select Artists.name, Albums.name, count(*) as num "
    #     "from Artists "
    #     "inner join Albums on Artists.id = Albums.artist_id "
    #     "inner join Songs on Songs.album_id = Albums.id "
    #     "group by Albums.id order by num desc limit 1 "
    # ):
    #     print(row)

#7total

    # for row in cur.execute(
    #     "select Artists.name, Albums.name, total(duration) as num "
    #     "from Artists "
    #     "inner join Albums on Artists.id = Albums.artist_id "
    #     "inner join Songs on Songs.album_id = Albums.id "
    #     "group by Albums.id "
    #     "order by num desc limit 1 "):
    #     print(row)



#8
#     for roe in cur.execute(
#         "select Artists.name, Albums.name, total(duration)/count(*) as num "
#         "from Artists "
#         "inner join Albums on Artists.id = Albums.artist_id "
#         "inner join Songs on Songs.album_id = Albums.id "
#         "group by Albums.id "
#         "order by num desc limit 1 "
# ):
#         print(roe)


#9

    # for roe in cur.execute(
    #     "select Artists.name, Albums.name, count(*) as num "
    #     "from Artists "
    #     "inner join Albums on Artists.id = Albums.artist_id "
    #     "inner join Songs on Songs.album_id = Albums.id "
    #     "inner join Listened on Listened.song_id = Songs.id "
    #     "group by Songs.id order by num desc limit 5 "
    # ):
    #     print(roe)


#10+

    # for roe in cur.execute(
    #     "select Albums.release_year, count(*) as num "
    #     "from Artists "
    #      "inner join Songs on Songs.album_id = Albums.id "
    #     "inner join Albums on Artists.id = Albums.artist_id "
    #     "inner join Listened on Listened.song_id = Songs.id "
    #     "group by Albums.release_year order by num desc limit 1 "
    # ):
    #     print(roe)


#11-

    for row in cur.execute(
        "select Artists.name, Albums.name, Songs.name, Listened.start_time "
        "from Artists "
        "inner join Albums on Artists.id = Albums.artist_id "
        "inner join Songs on Songs.album_id = Albums.id "
        "inner join Listened on Listened.song_id = Songs.id "
        "inner join Users on Users.id = Listened.user_id "
        "where Users.id = 47 "
        "order by Listened.start_time desc limit 20 "
     ):
        print(row)
















