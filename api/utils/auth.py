
import jwt, datetime

# Chave secreta para assinatura do token JWT
SECRET_KEY = "minha_chave_secreta"

# Função para gerar o token JWT
def gerar_token(user_id):
    try:
        # Define as informações a serem incluídas no token
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30) 
        } 

        # Gera o token com as informações acima e a chave secreta definida
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # Retorna o token como string
        return token

    except Exception as e:
        print(f"Erro ao gerar token: {str(e)}")