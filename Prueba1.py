from flask import Flask


app=Flask(__name__)


@app.route('/')
def hello():
  return("Hola Mundoooooooooooo!!!!!!!!!!!!!!!!!!!!")

@app.route('/ingresoNombre/<nombre>')
def imprimirNombre(nombre):
  nom=nombre
  return("Ingreso: "+ nombre)

@app.route('/ingresoApellido/<apellido>')
def imprimeApellido(apellido):
  ape=apellido
  return("Ingreso: "+ apellido)

@app.route('/datos')
def imprimeDatos():
  return ("datos: " + nom + ape )
