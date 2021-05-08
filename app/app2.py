from flask import Flask

app2 = Flask(__name__)


def index():
    return "Codigofacilito2"

if __name__ == '__main__':
    app2.add_url_rule('/',view_func=index)
    app2.run()