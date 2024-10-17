from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)

# Configurando o banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configurando o Redis para cache
r = redis.Redis(host='localhost', port=6379, db=0)


# Modelo para a Tarefa
class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	status = db.Column(db.String(20), default='pendente')


# Criando o banco de dados
with app.app_context():
	db.create_all()


# Função para validar o título da tarefa
def validate_task_data(data):
	if 'title' not in data or not data['title'].strip():
		return False
	return True


# Rota para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
	cached_tasks = r.get('tasks')
	if cached_tasks:
		return jsonify(eval(cached_tasks)), 200

	tasks = Task.query.all()
	tasks_list = [{'id': task.id, 'title': task.title, 'status': task.status} for task in tasks]

	r.set('tasks', str(tasks_list))
	return jsonify(tasks_list), 200


# Rota para adicionar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def add_task():
	data = request.get_json()

	if not validate_task_data(data):
		return jsonify({'error': 'Título da tarefa é obrigatório!'}), 400

	new_task = Task(title=data['title'])
	db.session.add(new_task)
	db.session.commit()
	r.delete('tasks')  # Limpa o cache

	return jsonify({'message': 'Tarefa adicionada com sucesso!'}), 201


# Rota para atualizar o status de uma tarefa
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
	task = Task.query.get(id)
	if not task:
		return jsonify({'error': 'Tarefa não encontrada!'}), 404

	data = request.get_json()
	task.status = data.get('status', task.status)
	db.session.commit()
	r.delete('tasks')  # Limpa o cache

	return jsonify({'message': 'Status da tarefa atualizado!'}), 200


# Rota para remover uma tarefa
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
	task = Task.query.get(id)
	if not task:
		return jsonify({'error': 'Tarefa não encontrada!'}), 404

	db.session.delete(task)
	db.session.commit()
	r.delete('tasks')  # Limpa o cache

	return jsonify({'message': 'Tarefa removida com sucesso!'}), 200


if __name__ == '__main__':
	app.run(debug=True)
