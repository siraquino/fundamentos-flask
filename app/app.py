from flask import Flask, render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    print('Antes de la peticion...')

@app.after_request
def after_request(response):
    print('Despues de la peticion...')
    return response

"""
@app.route('/')
def index():
    return render_template('index.html')
"""

def index():
    #return render_template('index.html',titulo='index enviado2')
    #para enviar varios parametros
    print('Estamos reaizando la peticion....')
    data = {
        'titulo':'index de data',
        'encabezado':'Bienvenido'
    }
    return render_template('index.html',data=data)

@app.route('/contacto')
def contacto():
    data = {
        'titulo':'Contacto',
        'encabezado':'Bienvenido'
    }
    return render_template('contacto.html',data=data)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return 'Hola, {0}!'.format(nombre)


@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1,valor2):
    return 'La suma es: {0}'.format((valor1 + valor2))

@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre,edad):
    return 'Tu nombre es: {0} y tu edad es: {1}'.format(nombre,edad)

@app.route('/lenguajes')
def lenguajes():
    data = {
        'hay_lenguajes':False,
        'lenguajes':['PHP','Python','kotlin','Java']
    }
    return render_template('lenguajes.html', data=data)

@app.route('/datos')
def datos():
    print(request.args)
    a = request.args.get('valor1')
    b = int(request.args.get('valor2'))
    return 'Esto son los datos: {0}, {1}'.format(a,b+15)

if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=5005)