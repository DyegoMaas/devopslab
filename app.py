from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app) # Compliant

@app.route("/")
def pagina_inicial():
    return "Hello World, Dyego Maas!"

if __name__ == '__main__':
    app.run()