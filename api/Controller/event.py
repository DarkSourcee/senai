from flask import Blueprint, jsonify, request
from Model.event import Event
from config.response import response
import jwt

event = Blueprint('event', __name__)

# Rota para listar todos os registros na tabela "usuarios"
@event.route('/event', methods=['GET'])
def listar_event():
    try:
        event = Event.listaEvent()
        return response(error="", data=event, status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)

# Rota para buscar um usuário pelo ID
@event.route('/event/<int:id>', methods=['GET'])
def buscar_event(id):
    try:
        event = Event.listaEventPorID(id)
        return jsonify(event)
    except:
        return response(error="Erro na consulta", data="", status=401)

# # Rota para cadastrar um novo evento
@event.route('/event', methods=['POST'])
def cadastrar_event():
    try:
        token = request.headers.get('Authorization')
        decoded_token = jwt.decode(token, 'minha_chave_secreta', algorithms=['HS256'])
        usuario_id = decoded_token['user_id']
        dados = {
            "nome" : request.json['nome'],
            "numero" : request.json['numero'],
            "dataAcontecimento" : request.json['dataAcontecimento'],
            "duracao" : request.json['duracao'],
            "id" : usuario_id
        }
        Event.cadastraEvent(dados)
        return response(error="", data="Evento cadastrado com sucesso!", status=200)    
    except KeyError:
        return response(error="Erro na inserção dados", data="", status=401)
    except Exception as e:
        return response(error=f"Erro ao autenticar usuário: {str(e)}", data="", status=401)

# # Rota para atualizar os dados de um evento pelo ID
@event.route('/event/<int:id>', methods=['PUT'])
def atualizar_event(id):
    try:
        dados = {
            "idEvent" : id,
            "nome" : request.json['nome'],
            "numero" : request.json['numero'],
            "dataAcontecimento" : request.json['dataAcontecimento'],
            "duracao" : request.json['duracao'],
        }
        Event.atualizarEvent(dados)
        return response(error="", data="Evento atualizado com sucesso!", status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)

# # Rota para excluir um usuário pelo ID
@event.route('/event/<int:id>', methods=['DELETE'])
def excluir_event(id):
    try:
        Event.deletarEvent(id)
        return response(error="", data="Evento excluído com sucesso!", status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)

