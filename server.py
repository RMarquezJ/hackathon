from flask import Flask, render_template

app = Flask(__name__)
'''
# turno 1
red_jinja = Unit('Red Ninja', 3, 3, 7)
# turno 2
hard_alg = Unit('Hard Algorithm', 2, 'resistencia', 3)
hard_alg.play(red_jinja)

cards = [red_jinja, hard_alg]
'''

objetos = [
    {
        'nombre': 'Pepe',
        'edad': 34
    },
    {
        'nombre': 'Juana',
        'edad': 23
    },
    {
        'nombre': 'Julia',
        'edad': 12
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html', objetos=objetos)


app.run()
