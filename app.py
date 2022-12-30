
from flask import Flask, jsonify, request
from data import usa_presidents

app = Flask(__name__)


# Retorna todos os registros metodo GET
@app.route('/presidentes', methods=['GET'])
def list_all_registers():
    return jsonify(usa_presidents)


# Retorna registro pela Id GET por Id
@app.route('/presidentes/<int:id>', methods=['GET'])
def register_by_id(id):
    response = {'404': 'Registro não encontrado'}
    status = 404
    for presidente in usa_presidents:
        if presidente.get('id') == id:
            status = 200
            return jsonify(presidente), status
    if status != 200:
        return jsonify(response)


# Altera Registro methodo PUT
@app.route('/presidentes/<int:id>', methods=['PUT'])
def edit_register_by_id(id):
    response = {'200': 'Alteração realizada com sucesso'}
    status = 404
    alter_register = request.get_json()
    for indice, presidente in enumerate(usa_presidents):
        if presidente.get('id') == id:
            status = 200
            usa_presidents[indice].update(alter_register)
            return jsonify(response), status
    if status != 200:
        response = {'404': 'Registro não encontrado'}
        return jsonify(response)


# Inclui Registro methodo POST
@app.route('/presidentes', methods=['POST'])
def insert_president():
    response = {'200': 'Inclusão realizada com sucesso'}
    new_president = request.get_json()
    usa_presidents.append(new_president)
    return jsonify(response)


# Exclui registro metodo DELETE
@app.route('/presidentes/<int:id>', methods=['DELETE'])
def del_president(id):
    response = {'200': 'Exclusão realizada com sucesso'}
    status = 404
    for indice, presidente in enumerate(usa_presidents):
        if presidente.get('id') == id:
            status = 200
            del usa_presidents[indice]
            return jsonify(response), status
    if status != 200:
        response = {'404': 'Registro não encontrado'}
        return jsonify(response)

# Start do server
app.run(port=5000, host='localhost', debug=False)
