import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app)  # Compliant


@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"


if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)