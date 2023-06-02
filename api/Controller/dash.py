from flask import Blueprint, jsonify, request
from Model.event import dash
from config.response import response
import jwt

event = Blueprint('dash', __name__)

@event.route('/event', methods=['GET'])
def buscar_eventPorUsuario():
    try:
        token = request.headers.get('Authorization')
        decoded_token = jwt.decode(token, 'minha_chave_secreta', algorithms=['HS256'])
        usuario_id = decoded_token['user_id']
        event = dash.listaEventPorUsuario(usuario_id)
        return jsonify(event)
    except:
        return response(error="Erro na consulta", data="", status=401)

@event.route('/eventUsuario', methods=['GET'])
def buscar_eventQtdePorUsuario():
    try:
        token = request.headers.get('Authorization')
        decoded_token = jwt.decode(token, 'minha_chave_secreta', algorithms=['HS256'])
        usuario_id = decoded_token['user_id']
        event = dash.listaQtdeEventPorUsuario(usuario_id)
        return jsonify(event)
    except:
        return response(error="Erro na consulta", data="", status=401)

@event.route('/eventTop', methods=['GET'])
def buscar_eventTop():
    try:
        event = dash.listaEventTop()
        return jsonify(event)
    except:
        return response(error="Erro na consulta", data="", status=401)