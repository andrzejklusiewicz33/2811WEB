from domain import *
import random
import psycopg2
import settings
# def get_all():
#     result=[]
#     for x in range(1,11):
#         p=Product(x,f'Nazwa produktu numer {x}',random.randint(1,200),f"Opis produktu numer {x}",random.randint(1,100))
#         result.append(p)
#     return result

def get_all():
    result = []
    with psycopg2.connect(host=settings.host, port=settings.port, database=settings.database, user=settings.user,password= settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute('select * from produkty')
        for w in cursor:
            product=Product(w[0],w[1],w[2],w[3],w[4])
            result.append(product)
    return result

def get_one(id):
    with psycopg2.connect(host=settings.host, port=settings.port, database=settings.database, user=settings.user,
                          password=settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute(f'select * from produkty where id_produktu={id}')
        w=cursor.fetchone()
        product = Product(w[0], w[1], w[2], w[3], w[4])
        return product
