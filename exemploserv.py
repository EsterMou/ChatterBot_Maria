from flask import Flask
from flask import jsonify

servico = Flask(__name__)

@servico.route("/info")
def get_info():
    return jsonify(
        version = "1.0",
        autor = "Ester Moura",
        email = "mouraester1998@gmail.com"
    )
    
@servico.route("/somar/<int:numero_a>/<int:numero_b>")
def somar(numero_a, numero_b):
    return str(numero_a + numero_b)

@servico.route("/subtrair/<int:numero_a>/<int:numero_b")
def subtrair(numero_a, numero_b):
    return str(numero_a - numero_b)

if __name__ == "__main__":
    servico.run()