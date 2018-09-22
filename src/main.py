from professor import professor
from student import student
from course import course
import pyodbc

def query(cnxn, sqlCommand):
    cnxn.execute(sqlCommand)
    cnxn.commit()

def createConnectionToDB():
    server = 'QICAI'
    database = 'student'
    username = 'sa'
    password = 'Fanhao1024'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return cnxn


if __name__ == "__main__":
    s2 = professor("li","hao",1)
    print(s2.firstName)



    cnxn = createConnectionToDB();
    s1 = course(1, "english", 40, 1)
    cmd = s1.insert();
    print(cmd)
    query(cnxn, cmd)
    s1 = course(2, "physics", 45, 2)
    cmd = s1.insert();
    query(cnxn, cmd)


    cursor = cnxn.cursor()
    cursor.execute("SELECT * from students;")
    row = cursor.fetchone()
    while row:
        print(row.firstName)
        print(row.lastName)
        print(row.id)
        row = cursor.fetchone()













