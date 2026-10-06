from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def domov():
    meno = "Janko"
    return render_template('index.html', meno=meno)


@app.route('/studenti')
def studenti():
    studenti = [
        {"meno": "Peter", "trieda": "2.A", "hodnotenie": 1},
        {"meno": "Lucia", "trieda": "2.A", "hodnotenie": 2},
        {"meno": "Jana", "trieda": "2.B", "hodnotenie": 1},
        {"meno": "Martin", "trieda": "2.B", "hodnotenie": 3},
        {"meno": "Simona", "trieda": "2.C", "hodnotenie": 2},
    ]
    return render_template('studenti.html', studenti=studenti)


@app.route('/prihlasenie')
def prihlasenie():
    prihlaseny = True
    return render_template('prihlasenie.html', prihlaseny=prihlaseny)
