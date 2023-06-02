from flask import Flask
from Controller.usuarios import usuarios
from Controller.event import event
from Controller.dash import dash

app = Flask(__name__)
app.register_blueprint(usuarios) 
app.register_blueprint(event)
app.register_blueprint(dash)

if __name__ == '__main__':
    app.run(debug=True)
