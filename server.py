from flask import Flask, render_template

from cards import Cards
from cards import Units
from cards import Effects

app = Flask(__name__)

red_ninja = Units('Red Belt Ninja', 3, 3, 4)
black_ninja = Units('Black Belt Ninja', 4, 5, 4)
hard_algorithm = Effects('Hard Algorithm', 2, 'resistance', 3)
not_managed_promise = Effects('Not Managed Promise', 1, 'resistance', -2)
pair_programming = Effects('Pair Programming', 3, 'power', 2)

red_ninja.play(1)
hard_algorithm.affect(red_ninja)
black_ninja.play(2)
not_managed_promise.affect(red_ninja)
pair_programming.affect(red_ninja)
red_ninja.attack(black_ninja)

objetos = [
red_ninja,
black_ninja,
hard_algorithm,
not_managed_promise,
pair_programming
]

@app.route("/")
def hello_world():
    return render_template('index.html', objetos=objetos)


app.run(debug=True)
