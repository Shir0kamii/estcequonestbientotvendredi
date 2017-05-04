from datetime import datetime
from flask import Flask, render_template

app = Flask("estcequonestbientotvendredi")

day_table = [
    "Si t'es ici, tu commences mal la semaine...",
    "Non.",
    "Presque.",
    "Bientôt.",
    "On est vendredi, tout est permis.",
    "Raté, c'était hier.",
    "Reviens la semaine prochaine."
]


@app.route("/")
def test():
    now = datetime.now()
    return render_template("template.html", msg=day_table[now.weekday()])


if __name__ == '__main__':
    app.run(port=8000, debug=True)
