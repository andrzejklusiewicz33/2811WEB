from faker import Faker
faker=Faker("pl_PL")
from domain import *
import psycopg2

# def get_all():
#     result=[]
#     for x in range(1,6):
#         e=Employee(x,faker.first_name(),faker.last_name())
#         result.append(e)
#     return result

def get_all():
    result=[]
    with psycopg2.connect(host="localhost",port=5432,database="andrzej",user="andrzej",password="oracle") as connection:
        cursor=connection.cursor()
        cursor.execute('select * from pracownicy')
        for w in cursor:
            employee=Employee(w[0],w[1],w[2])
            result.append(employee)
    return result