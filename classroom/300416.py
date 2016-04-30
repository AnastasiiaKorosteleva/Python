__author__ = 'anastasiiakorosteleva'

import sqlite3 as sq

with sq.connect("tmp.sqlite") as connection:
    cursor = connection.cursor()

    for row in cursor.execute(
            "select students.name, year, courses.name, score, count(*), sum(score) from participation "
            "inner join students on student_id = students.id "
            "inner join courses on course_id = courses.id "
            # "where year = '2014' and score >= 4 "
            "group by students.id"):
       # print(row[0], row[1], row[2], row[3])
        print(row)
