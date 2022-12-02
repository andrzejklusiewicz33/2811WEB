from faker import Faker
faker=Faker("pl_PL")
from domain import *

def get_all():
    result=[]
    for x in range(1,6):
        e=Employee(x,faker.first_name(),faker.last_name())
        result.append(e)
    return result