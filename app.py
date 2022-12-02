from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show_products')
def show_products():
    return render_template("show_products.html")

@app.route('/about')
def about():
    return render_template("about.html",first_name="Andrzej",last_name="Klusiewicz",email="klusiewicz@jsystems.pl")

class Owoc:
    def __init__(self,nazwa,kolor):
        self.nazwa=nazwa
        self.kolor=kolor
    def __str__(self):
        return str(self.__dict__)

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