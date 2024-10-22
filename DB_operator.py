import json
import os
import pyodbc
from dotenv import load_dotenv
import SQL_Queries


class ConnectDB:
    @staticmethod
    def connect_to_db(server, database, user, password):
        ConnectionString = f'''DRIVER={{SQL Server}};
                               SERVER={SERVER};
                               DATABASE={DATABASE};
                               Trusted_Connections=yes'''
        try:
            conn = pyodbc.connect(ConnectionString)
            conn.autocommit = True
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            return conn


class MSSQLOperator:

    def __init__(self, connector_obj):
        self.conn = connector_obj

    def select_from_table(self, database_name, sql_query):
        cursor = self.conn.cursor()
        cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query
        try:
            cursor.execute(SQL_Query)
        except pyodbc.ProgrammingError as ex:
            return ex
        else:
            columns = [column[0] for column in cursor.description]
            values = cursor.fetchone()
            row_dict = dict(zip(columns, values))
            return row_dict


if __name__ == "__main__":
    load_dotenv()
    SERVER = os.getenv('MS_SQL_SERVER')
    DATABASE = os.getenv('MS_SQL_DATABASE')
    USER = os.getenv('MS_SQL_USER')
    PASSWORD = os.getenv('MS_SQL_KEY')
    academy = "academy_database"
    fv = "Овощи_и_фрукты"
    fitnes_club = "Фитнес_клуб"

    my_conn = ConnectDB.connect_to_db(SERVER, DATABASE, USER, PASSWORD)
    my_db_operator = MSSQLOperator(my_conn)

    with open('Данные_запросов.json', mode='w', encoding="UTF-8") as file:
        file.write("[")
        dictionary = my_db_operator.select_from_table(academy, SQL_Queries.select_exist_1())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(fitnes_club, SQL_Queries.select_exist_2())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(academy, SQL_Queries.select_any())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(fv, SQL_Queries.select_some())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(academy, SQL_Queries.select_all())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(academy, SQL_Queries.select_anysome_all())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(fv, SQL_Queries.select_union())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(fv, SQL_Queries.select_union_all())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(academy, SQL_Queries.select_innerjoin())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(fitnes_club, SQL_Queries.select_leftjoin())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(fv, SQL_Queries.select_rightjoin())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(academy, SQL_Queries.select_leftrightjoin())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write(",")
        dictionary = my_db_operator.select_from_table(fv, SQL_Queries.select_fulljoin())
        json.dump(dictionary, file, ensure_ascii=False)
        file.write("]")
