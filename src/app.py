from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)  
    return jsonify(todos) 

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        todos.pop(position)  
        return jsonify(todos), 
    else:
        return jsonify({"": ""}), 

if __name__ == '__main__':
    app.run(debug=True)
