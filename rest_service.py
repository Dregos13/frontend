import flask
from flask import request, jsonify
import database

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
	return jsonify({'message': 'Hello '+name, 'success': True})

@app.route('/hello/<name>/<times>', methods=['GET'])
def hello_times(name, times):
	return jsonify([name] * int(times))

@app.route('/caracola', methods=['GET'])
def caracola():
	return jsonify('Hola')

@app.route('/users',methods=['GET'])
def muestraUsuarios():
	arg = "SELECT * FROM employees"
	resul = database.function(arg)
	lista=[]
	for row in resul:
		lista.append({'id': int(row[0]),'nombre':row[1],'apellido':row[2],'salario':row[3]})
	arg = "SELECT * FROM cliente"
	resul1 = database.function(arg)
	lista1=[]
	for row in resul1:
		lista1.append({'nombre': row[0],'id':int(row[1]),'empleado asignado':int(row[2])})
	return jsonify({'message': 'Empleados'},lista,{'message': 'Clientes'},lista1)

@app.route('/users/<id>/activate',methods=['GET'])
def muestraUsuarioPorID(id):
	arg = ("SELECT * FROM employees WHERE id=" + id)
	database.function(arg)
	return jsonify('done')

@app.route('/users',methods=['POST'])
def muestraUsuariosSeguro():
	arg = ("SELECT * FROM employees")
	database.function(arg)
	return jsonify('done')

@app.route('/users/<id>/<pay>',methods=['PATCH'])
def cambiarSalario(id,pay):
	arg = ("UPDATE employees SET SALARIO='"+pay+"' WHERE id='"+id+"'")
	database.function2(arg)
	return jsonify('done')

@app.route('/ceu/<id>/<employee>',methods=['PATCH'])
def cambiarEmpleado(id,employee):
	arg = ("UPDATE cliente SET empleado='"+employee+"' WHERE id='"+id+"'")
	database.function2(arg)
	return jsonify('done')

@app.route('/ic/<name>/<employee>/<apellido>/<dni>/<nacimiento>',methods=['PATCH'])
def insertarCliente(name,employee,apellido,dni,nacimiento):
	arg = ("INSERT INTO cliente (nombre, empleado, apellido, dni, birthday) VALUES ('"+name+"','" + employee + "','" + apellido + "','" + dni +"','" + nacimiento + "')")
	database.function2(arg)
	return jsonify('done')

@app.route('/ie/<name1>/<name2>/<pay>/<bd>/<dni>',methods=['PATCH'])
def insertarEmpleado(name1,name2,pay,bd,dni):
	arg = ("INSERT INTO employees (first_name,last_name,salario,birthday,dni) VALUES ('"+name1+"','" + name2 + "','" + pay + "','" + bd + "','" + dni + "')")
	database.function2(arg)
	return jsonify('done')

@app.route('/dc/<id>',methods=['PATCH'])
def borrarCliente(id):
	arg = ("DELETE FROM cliente WHERE id='"+id+"'")
	database.function2(arg)
	return jsonify('done')

@app.route('/de/<id>',methods=['PATCH'])
def borrarEmpleado(id):
	arg = ("DELETE FROM employees WHERE id='"+id+"'")
	database.function2(arg)
	return jsonify('done')

app.run()