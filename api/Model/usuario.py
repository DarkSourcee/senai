from config.database import mydb

class Usuario:
    def listaUsuarios():
        cursor = mydb.cursor() 
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
        return usuarios
    
    def listaUsuariosPorID(id):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM usuario WHERE id=%s", (id,))
        usuario = cursor.fetchone()
        return usuario
    
    def cadastraUsuario(dados):
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO usuario (nome, email, login, senha) VALUES (%s, %s, %s, %s)", (dados["nome"], dados["email"], dados["login"], dados["senha"]))
        usuario = mydb.commit()
        return usuario
    
    def atualizarUsuario(dados):
        cursor = mydb.cursor()
        cursor.execute("UPDATE usuario SET nome=%s, login=$s, email=%s, senha=%s WHERE id=%s", (dados["nome"], dados["login"], dados["email"], dados["senha"], dados["id"]))
        usuario = mydb.commit()
        return usuario
    
    def deletarUsuario(id):
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM usuario WHERE id=%s", (id,))
        usuario = mydb.commit()
        return usuario
    
    def verificaLogin(dados):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM usuario WHERE login=%s AND senha=%s",(dados.get("login"), dados.get("senha")))
        usuario = cursor.fetchone()
        
        if not usuario:
            return None
        
        usuario_dict = {
            "id": usuario[0],
            "nome": usuario[1],
            "email": usuario[2],
            "login": usuario[3],
            "senha": usuario[4]
        }
        
        return usuario_dict
