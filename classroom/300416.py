__author__ = 'anastasiiakorosteleva'
import sqlite3 as sq
# postgresql
import psycopg2 # implements DB API v2.0


with sq.connect("tmp.sqlite") as con:  # открыли соединение с базой данных
    cur = con.cursor()  # получили курсор

    в этом примере мы вывели топ-5 студентов ИБ по среднему рейтингу
    по всем курсам
    for row in cur.execute(
            "select students.name, year, " # что выбрать в ответ, исполняется последним
            "sum(score) * 1.0 / count(*) as avg "  # назвали данный столбец avg
            "from participation "  # откуда выбрать
            "inner join students " # inner join "сливает" таблицы вместе
            "on student_id = students.id "  # по данному правилу
            "inner join courses "  # добавили ещё одну таблицу
            "on course_id = courses.id " # по данному правилу
            "group by students.id "  # сгруппировали выдачу по отдельным студентам
            "order by avg desc "  # отсортировали по среднему баллу
            "limit 5"):  # оставили только 5 верхних значений
        print(row)

    # а в этом примере мы посчитали средний балл по курсу за каждый год
    for row in cur.execute(
            "select courses.name, year, sum(score) * 1.0 / count(*) "
            "from participation "
            "inner join students "
            "on student_id = students.id "
            "inner join courses "
            "on course_id = courses.id "
            "group by course_id, year"):  # группировать можно и по паре значений
        print(row)