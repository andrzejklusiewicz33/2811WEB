from domain import *
import random

def get_all():
    result=[]
    for x in range(1,11):
        p=Product(x,f'Nazwa produktu numer {x}',random.randint(1,200),f"Opis produktu numer {x}",random.randint(1,100))
        result.append(p)
    return result