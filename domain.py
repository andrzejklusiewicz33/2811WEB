class Author:
    def __init__(self,first_name,last_name,email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

class Owoc:
    def __init__(self,nazwa,kolor):
        self.nazwa=nazwa
        self.kolor=kolor
    def __str__(self):
        return str(self.__dict__)


class Employee:
    def __init__(self,employee_id,first_name,last_name):
        self.employee_id=employee_id
        self.first_name=first_name
        self.last_name=last_name
    def __str__(self):
        return str(self.__dict__)