from config.database import mydb

class dash:
    def listaEventPorUsuario(id):
        cursor = mydb.cursor()
        cursor.execute("SELECT e.* FROM event e left join usuarios u on u.id = e.idUsuario WHERE e.idUsuario=%s", (id,))
        event = cursor.fetchone()
        return event

    def listaQtdeEventPorUsuario(id):
        cursor = mydb.cursor()
        cursor.execute("SELECT count(e.idEvent) qtdeEvent, u.nome FROM event e left join usuarios u on u.id = e.idUsuario WHERE e.idUsuario=%s group by u.nome", (id,))
        event = cursor.fetchone()
        return event 

    def listaEventTop(id):
        cursor = mydb.cursor()
        cursor.execute("SELECT TOP 10 * FROM event ORDER BY dataAcontecimento")
        event = cursor.fetchone()
        return event 