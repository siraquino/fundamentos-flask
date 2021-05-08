from flask import Flask

app3 = Flask(__name__)


def index():
    return "Codigofacilito3"


@app3.route('/holamundo')
def hola_mundo():
    return "Hola MUndo"


if __name__ == '__main__':
    app3.add_url_rule('/', view_func=index)
    app3.run(debug=True, port=5005)
