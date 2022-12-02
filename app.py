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
    return render_template("about.html")

@app.route('/tests')
def tests():
    x=99
    krotka=("Python",'Java','PL/SQL','PL/pgSQL')
    return render_template("tests.html",zmienna=x, jezyki=krotka)  #"<h1>Strona testowa - zmieniona SIEMA TU MAPET!</h1>"



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