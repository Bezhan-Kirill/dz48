def select_exist_1():
    QUERY = fr"""
            SELECT *
            FROM Students
            WHERE EXISTS(SELECT русский_язык
            FROM Grades
            WHERE date = '2024-07-10' AND Students.id = Grades.students_id);"""
    return QUERY


def select_exist_2():
    QUERY = fr"""
            SELECT Имя + ' ' + Фамилия
            FROM Посетители
            WHERE EXISTS(
                SELECT Журнал_посещений.id_посетителя
                FROM Журнал_посещений
                WHERE Журнал_посещений.id_занятия = 1 AND Журнал_посещений.id_посетителя = Посетители.id_посетителя);"""
    return QUERY


def select_any():
    QUERY = fr"""
            SELECT firstname + lastname
            FROM Students
            WHERE id = ANY(SELECT students_id
                FROM Grades
                WHERE литература = 5);"""
    return QUERY


def select_some():
    QUERY = fr"""
            SELECT *
            FROM Фрукты
            WHERE Цвет = SOME(
                SELECT Цвет
                FROM Фрукты
                WHERE Цвет = 'Красный');"""
    return QUERY


def select_all():
    QUERY = fr"""
            SELECT firstname + ' ' + lastname, химия
            FROM Students, Grades
            WHERE Students.id = Grades.students_id AND
                химия > ALL (SELECT AVG(Grades.химия)
                FROM Grades);"""
    return QUERY


def select_anysome_all():
    QUERY = fr"""
            SELECT firstname + ' ' + lastname, химия
            FROM Students, Grades
            WHERE Students.id = Grades.students_id AND химия = ANY(
                SELECT химия
                FROM Grades
                WHERE химия > ALL (SELECT AVG(Grades.химия)
                FROM Grades));"""
    return QUERY


def select_union():
    QUERY = fr"""
            SELECT Фрукты.Калории , Фрукты.Название
            FROM Фрукты
            WHERE Калории >= 50
            UNION
            SELECT Овощи.Калории, Овощи.Название
            FROM Овощи
            WHERE Калории >= 50"""
    return QUERY


def select_union_all():
    QUERY = fr"""
            SELECT Фрукты.Название + Поставщики.Наименование, Поставщики.Страна
            FROM Фрукты, Поставщики
            WHERE Фрукты.id_поставщика = Поставщики.id
            UNION ALL
            SELECT Овощи.Название + Поставщики.Наименование, Поставщики.Страна
            FROM Овощи, Поставщики
            WHERE Овощи.id_поставщика = Поставщики.id"""
    return QUERY


def select_innerjoin():
    QUERY = fr"""
            SELECT *
            FROM Groups INNER JOIN Students
            ON Groups.group_id=Students.group_id"""
    return QUERY


def select_leftjoin():
    QUERY = fr"""
            SELECT *
            FROM Посетители LEFT JOIN Секции
            ON Посетители.id_секции = Секции.id_секции"""
    return QUERY


def select_rightjoin():
    QUERY = fr"""
            SELECT *
            FROM Поставщики RIGHT JOIN Овощи
            ON Овощи.id_поставщика = Поставщики.id"""
    return QUERY


def select_leftrightjoin():
    QUERY = fr"""
            SELECT *
            FROM Grades LEFT JOIN Students
            ON Grades.students_id = Students.id RIGHT JOIN Groups
            ON Groups.group_id = Students.group_id"""
    return QUERY


def select_fulljoin():
    QUERY = fr"""
            SELECT *
            FROM Поставщики FULL JOIN Фрукты
            ON Фрукты.id_поставщика = Поставщики.id"""
    return QUERY
