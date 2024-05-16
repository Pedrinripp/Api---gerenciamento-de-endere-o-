from flask import Flask, jsonify, request

app = Flask(__name__)

enderecos=[
    {
        'id': 1,
        'cep': '04013-002',
        'rua': 'Rua cubatao',
        'numero': '726'
    },
        {
        'id': 2,
        'cep': '04018-01',
        'rua': 'Rua doutor alvaro',
        'numero': '90'
    },
        {
        'id': 3,
        'cep': '18087-101',
        'rua': 'Avenida idependencia',
        'numero': '210'
    },
]

@app.route('/enderecos', methods=['GET'])
def obter_endereco():
    return jsonify(enderecos)

@app.route('/endereco/<int:id>', methods=['GET'])
def obter_endereco_por_id(id):
    for endereco in enderecos:
        if endereco.get('id') == id:
            return jsonify(endereco) 
        
@app.route('/enderecos/<int:id>',methods=['PUT'])
def editar_endereco_por_id(id):
    endereco_alterado = request.get_json()
    for indice,endereco in enumerate(enderecos):
        if endereco.get('id') == id:
            enderecos[indice].update(endereco_alterado)
            return jsonify(enderecos[indice])
        
@app.route('/endereco', methods=['POST'])
def incluir_novo_endereco():
    novo_endereco = request.get_json()
    enderecos.append(novo_endereco)

    return jsonify(enderecos)

@app.route('/endereco/<int:id>',methods=['DELETE'])
def excluir_endereco(id):
    for indice, endereco in enumerate(enderecos):
        if endereco.get('id') == id:
            del enderecos[indice]

    return jsonify(enderecos)


app.run(port=5000,host='localhost',debug=True)