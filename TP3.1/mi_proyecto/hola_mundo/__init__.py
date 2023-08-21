from flask import Flask, request
from config import Config
from datetime import datetime
import json
from pilas import Stack, balanceador


def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER)
    app.config.from_object(Config)

    @app.route('/')   #Ejercicio 1
    def index():
        return 'Bienvenidx!'

    @app.route('/info')   #Ejercicio 2
    def info():
        return f'Bienvenidx! a {app.config["APP_NAME"]}'

    @app.route('/about')  #Ejercicio 3
    def about():
        info = {
            'name': app.config['APP_NAME'],
            'descripcion': app.config['APP_DESCRIPTION'],
            'desarrolladores': app.config['APP_DEVELOPERS'],
            'version': app.config['APP_VERSION']
        }
        return info
    
    @app.route('/sum/<int:num1>/<int:num2>')  #Ejercicio 4
    def suma(num1, num2):
        return f'La suma de {num1} y {num2} es {num1+num2}'

    @app.route('/age/<dob>')  #Ejercicio 5
    def age(dob):
        try:
            dob_fecha = datetime.strptime(dob, '%Y-%m-%d')
            fecha_actual = datetime.now()
            if dob_fecha > fecha_actual:
                error = {'error': 'Todavía no naciste'}
                return error, 400
            edad = fecha_actual.year - dob_fecha.year
            if (fecha_actual.month, fecha_actual.day)<(dob_fecha.month, dob_fecha.day):
                return str(edad -1)
            else:
                return str(edad)
        except ValueError:
            error_formato = {'error': 'Formato de fecha invalido, prueba de la siguiente manera YYYY-MM-DD'}
            return error_formato, 400
        
    # @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')  #Ejercicio 6       (Está comentado ya que el 7 es el mismo pero con query parameters)
    # def operate(operation, num1, num2):
    #     if operation == 'sum':
    #         return f'La suma de {num1} y {num2} es {num1+num2}'
    #     elif operation == 'sub':
    #         return f'La resta de {num1} y {num2} es {num1-num2}'
    #     elif operation == 'mult':
    #         return f'La multiplicación de {num1} y {num2} es {num1*num2}'
    #     elif operation == 'div':
    #         if num2 == 0:
    #             error = {'error': 'La division no está definida para esos valores'}
    #             return error, 400
    #         else:
    #             return f'La division de {num1} y {num2} es {num1/num2}'
    #     else:
    #         error_msg = {'error': 'No existe ruta definida para ese endpoint'}
    #         return error_msg, 400

    @app.route('/operate')  #Ejercicio 7
    def operate():
        operation = request.args.get('operation')
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        if operation == 'sum':
            return f'La suma de {num1} y {num2} es {num1+num2}'
        elif operation == 'sub':
            return f'La resta de {num1} y {num2} es {num1-num2}'
        elif operation == 'mult':
            return f'La multiplicación de {num1} y {num2} es {num1*num2}'
        elif operation == 'div':
            if num2 == 0:
                error = {'error': 'La division no está definida para esos valores'}
                return error, 400
            else:
                return f'La division de {num1} y {num2} es {num1/num2}'
        else:
            error_msg = {'error': 'No existe ruta definida para ese endpoint'}
            return error_msg, 400

    @app.route('/title/<string:word>') #Ejercicio 8
    def title(word):
        letra_capital = word[0].upper()
        resto = word[1:].lower()
        formatted_word = letra_capital + resto
        palabra = {'formatted_word': formatted_word}
        return palabra

    @app.route('/formatted/<string:dni>') #Ejercicio 9
    def formatted(dni):
        dni_limpio = ''
        for char in dni:
            if char.isdigit():
                dni_limpio += char
        if len(dni_limpio) != 8 or dni_limpio.startswith('0'):
            error_msg = {'error': 'El DNI no es valido'}
            return error_msg, 400
        formatted_dni = int(dni_limpio)
        respuesta = {'formatted_dni': formatted_dni}
        return respuesta
    
    @app.route('/format') #Ejercicio 10
    def format():
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        dob = request.args.get('dob')
        dni = request.args.get('dni')

        formatted_firstname = firstname.title() #Podría haber usado el mismo método el ejercicio 8, pero esto es más simple.
        formatted_lastname = lastname.title()

        dob_fecha = datetime.strptime(dob, '%Y-%m-%d')
        fecha_actual = datetime.now()
        if dob_fecha > fecha_actual:
            error = {'error': 'Todavía no naciste'}
            return error, 400
        edad = fecha_actual.year - dob_fecha.year
        if (fecha_actual.month, fecha_actual.day)<(dob_fecha.month, dob_fecha.day):
            formatted_dob = str(edad -1)
        else:
            formatted_dob = str(edad)
        
        dni_limpio = ''
        for char in dni:
            if char.isdigit():
                dni_limpio += char
        if len(dni_limpio) != 8 or dni_limpio.startswith('0'):
            error_msg = {'error': 'El DNI no es valido'}
            return error_msg, 400
        formatted_dni = int(dni_limpio)
        respuesta = {
            'firstname': formatted_firstname,
            'lastname': formatted_lastname,
            'age': formatted_dob,
            'dni': formatted_dni
            }
        return respuesta
        
    @app.route('/encode/<string:keyword>') #Ejercicio 11
    def encode(keyword):
        keyword = keyword.upper()
        with open('hola_mundo/static/morse_code.json', 'r') as fo:
            morse = json.load(fo)
            codigo_resultado = ''
            for char in keyword:
                if char == '+':
                    codigo_resultado += '^+'
                elif char in morse['letters']:
                    codigo_resultado += morse['letters'][char] + '+'
                elif char.isdigit():
                    codigo_resultado += morse['letters'][char] + '+'
            codigo_resultado = codigo_resultado[:-1]
        if len(keyword) > 100:
            error_msg = {'error': 'La palabra supera los 100 caracteres'}
            return error_msg, 400
        return codigo_resultado

    @app.route('/decode/<string:morse_code>') #Ejercicio 12
    def decode(morse_code):
        with open('hola_mundo/static/morse_code.json', 'r') as fo:
            morse_data = json.load(fo)
            texto_decodificado = ''
            palabras = morse_code.split('^')
            for palabra in palabras:
                letras = palabra.split('+')
                palabra_decodificada = ''
                for letra in letras:
                    if letra in morse_data['letters'].values():
                        clave = [key for key, value in morse_data['letters'].items() if value == letra][0]
                        palabra_decodificada += clave
                        print(palabra_decodificada)
                    else:
                        print('no found')
                texto_decodificado += palabra_decodificada + ' '
        frase_decodificada = texto_decodificado.strip()
        return frase_decodificada

    @app.route('/convert/binary/<string:num>') #Ejercicio 13
    def convert(num):
        decimal = 0
        exp = 0
        for digito in reversed(num):
            if digito == '1':
                decimal += 2**exp
            exp += 1
        return str(decimal)

    @app.route('/balance/<string:input>') #Ejercicio 14
    def balance(input):
        if balanceador(input):
            return {'balanced': True}
        else:
            return {'balanced': False}

    return app