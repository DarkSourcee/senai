from config.database import mydb

class Event:
    def listaEvent():
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM event")
        event = cursor.fetchall()
        return event
    
    def listaEventPorID(id):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM event WHERE idEvent=%s", (id,))
        event = cursor.fetchone()
        return event
    
    def cadastraEvent(dados):
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO event(nome, numero, dataAcontecimento, duracao, idUsuario) VALUES (%s, %s, %s, %s, %s)", (dados["nome"], dados["numero"], dados["dataAcontecimento"], dados["duracao"] dados["id"]))
        event = mydb.commit()
        return event
    
    def atualizarEvent(dados):
        cursor = mydb.cursor()
        cursor.execute("UPDATE event SET nome=%s, numero=%s, dataAcontecimento=%s, duracao=%s WHERE idEvent=%s", (dados["nome"], dados["numero"], dados["dataAcontecimento"], dados["duracao"] dados["idEvent"]))
        event = mydb.commit()
        return event
    
    def deletarEvent(id):
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM event WHERE idEvent=%s", (id,))
        event = mydb.commit()
        return event