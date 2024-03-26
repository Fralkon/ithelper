from django.db import connection

def ReFillBD() :
        with connection.cursor() as cursor:
                cursor.execute("UPDATE hello_person SET name ='Tomas' WHERE name='Tom' AND age=22")
                cursor.execute("SELECT * FROM hello_person WHERE name = 'Tomas'")
                row = cursor.fetchone()     # получаем одну строку
                print(row)