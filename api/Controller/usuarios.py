from flask import Blueprint, jsonify, request
from utils.auth import gerar_token
from Model.usuario import Usuario
from config.response import response

usuarios = Blueprint('usuarios', __name__)

# Rota para listar todos os registros na tabela "usuarios"
@usuarios.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        usuarios = Usuario.listaUsuarios()
        return response(error="", data=usuarios, status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)

# Rota para buscar um usuário pelo ID
@usuarios.route('/usuarios/login', methods=['POST'])
def verificaLogin():
    try:
        dados = {
            "login" : request.json['login'],
            "senha" : request.json['senha'] 
        }
        
        usuario = Usuario.verificaLogin(dados)
        if not usuario:
            return response(error="Usuário e/ou senha não existem", data="", status=401)
            
        token = gerar_token(usuario.get("id"))
        return jsonify({'token': token})
    except KeyError:
        return response(error="Dados de login inválidos", data="", status=401)
    except Exception as e:
        return response(error=f"Erro ao autenticar usuário: {str(e)}", data="", status=401)

# Rota para buscar um usuário pelo ID
@usuarios.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario(id):
    try:
        usuario = Usuario.listaUsuariosPorID(id)
        return jsonify(usuario)
    except:
        return response(error="Erro na consulta", data="", status=401)

# # Rota para cadastrar um novo usuário
@usuarios.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    try:
        dados = {
            "nome" : request.json['nome'],
            "email" : request.json['email'],
            "login" : request.json['login'],
            "senha" : request.json['senha']      
        }
        Usuario.cadastraUsuario(dados)
        return response(error="", data="Usuário cadastrado com sucesso!", status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)

# # Rota para atualizar os dados de um usuário pelo ID
@usuarios.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    try:
        dados = {
            "id" : id, 
            "nome" : request.json['nome'],
            "email" : request.json['email'],
            "login" : request.json['login'],
            "senha" : request.json.get('senha')
        }
        Usuario.atualizarUsuario(dados)
        return response(error="", data="Usuário atualizado com sucesso!", status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)

# # Rota para excluir um usuário pelo ID
@usuarios.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    try:
        Usuario.deletarUsuario(id)
        return response(error="", data="Usuário excluído com sucesso!", status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)
