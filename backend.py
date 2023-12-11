#usando Flask para um backend simplificado do Conexão Saúde:

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conexaosaudedb.db'
db = SQLAlchemy(app)

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rg = db.Column(db.String(20), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)

@app.route('/cadastrar_paciente', methods=['POST'])
def cadastrar_paciente():
    dados_paciente = request.get_json()

    novo_paciente = Paciente(
        rg=dados_paciente['rg'],
        cpf=dados_paciente['cpf'],
        endereco=dados_paciente['endereco'],
        nome=dados_paciente['nome'],
        data_nascimento=dados_paciente['data_nascimento']
    )

    db.session.add(novo_paciente)
    db.session.commit()

    return jsonify({'message': 'Paciente cadastrado com sucesso!'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


Certifique-se de instalar o Flask e o Flask-SQLAlchemy antes de executar o código:

bash
pip install Flask Flask-SQLAlchemy

#inclui um banco de dados SQLite para armazenar informações do paciente e utiliza a extensão Flask-SQLAlchemy para interagir com o banco de dados.

#cadastro: 

from flask import Flask, request, jsonify

app = Flask(_name_)

pacientes = []

@app.route('/cadastrar_paciente', methods=['POST'])
def cadastrar_paciente():
    dados_paciente = request.get_json()

    rg = dados_paciente.get('rg')
    cpf = dados_paciente.get('cpf')
    endereco = dados_paciente.get('endereco')
    nome = dados_paciente.get('nome')
    data_nascimento = dados_paciente.get('data_nascimento')

    paciente = {
        'rg': rg,
        'cpf': cpf,
        'endereco': endereco,
        'nome': nome,
        'data_nascimento': data_nascimento
    }

    pacientes.append(paciente)

    return jsonify({'message': 'Paciente cadastrado com sucesso!'})

if _name_ == '_main_':
    app.run(debug=True)