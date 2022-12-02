from flask import Flask,render_template
from domain import *
import random
import employees_dao as edao

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

class Product:
    def __init__(self,product_id,name,price,description,stock):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.description=description
        self.stock=stock
    def __str__(self):
        return str(self.__dict__)

def get_all():
    result=[]
    for x in range(1,11):
        p=Product(x,f'Nazwa produktu numer {x}',random.randint(1,200),f"Opis produktu numer {x}",random.randint(1,100))
        result.append(p)
    return result

@app.route('/show_products')
def show_products():
    for p in get_all():
        print(p)
    return render_template("show_products.html")



@app.route('/about')
def about():
    author=Author('Andrzej','Klusiewicz','klusiewicz@jsystems.pl')
    return render_template("about.html", author=author)
    #return render_template("about.html",first_name="Andrzej",last_name="Klusiewicz",email="klusiewicz@jsystems.pl")


@app.route('/show_employees')
def show_employees():
    for e in edao.get_all():
        print(e)
    return render_template("show_employees.html")


@app.route('/tests')
def tests():
    x=99
    krotka=("Python",'Java','PL/SQL','PL/pgSQL')
    owoc=Owoc('Banan','Żółty')
    return render_template("tests.html",zmienna=x, jezyki=krotka,owoc=owoc)



if __name__ == '__main__':
    app.run(debug=True,port=80)

#52. Dodaj funkcje obslugujaca requesty na adresy: /show_products /about
#Zmien nazwę funkcji obslugujacej stronę główną na index(). Każda z funkcji
#powinna użytkownikowi wyświetlić jakiś tekst informujacy gdzie jest.
#Włącz tryb debug dla swojej aplikacji

#53. Zadbaj o to by każdy z ekranów pokazywał swój plik html z odpowiednim nagłówkiem


#przerwa do 11:45

#54. Zadbaj o to, by na wszystkich ekranach bylo menu z linkami do wszystkich podstron

#55. Przekaż do widoku ekranu /about swoje imię, nazwisko i email i wyświetl na widoku w tabeli

#56. Stwórz klasę Author i dodaj do niej konstruktor sparametryzowany. Klasa powinna
#posiadać pola first_name,last_name,email. W kontrolerze ekranu /about stwórz obiekt tej klasy,
#przekaż go do widoku i wyświetl dane z niego zamiast korzystac ze zmiennych z poprzedniego cwiczenia
#przekazywanie zmiennych z poprzedniego cwiczenia mozessz wtedy usunac


#PRZERWA OBIADOWA DO 13:25

#57. Dodaj klasę Product która będzie odwzorowywała dane z tabeli produkty w bazie. Dodaj też
#funkcję get_all() która zwróci kilka fejkowych produktów. Zadbaj o to by po wejściu na
#ekran /show_products na konsoli wyswietlily sie linia po linii obiekty z funkcji get_all()

#58.Przenies klasę Product do domain.py
# Przenieś funkcję get_all zwracajaca liste pracownikow do osobnego modulu product_dao.
#Zadbaj o to by po wejsciu na liste produktow nadal wyswietlaly sie na konsoli dane
