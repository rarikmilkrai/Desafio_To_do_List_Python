// URL da API
//const apiUrl = 'http://127.0.0.1:5000/tasks';
// URL da API
const apiUrl = 'http://192.168.10.7:5000/tasks';

// Carrega todas as tarefas na inicialização
window.onload = () => {
    loadTasks();
};

// Função para carregar as tarefas
function loadTasks() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(tasks => {
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = '';  // Limpa a lista de tarefas

            if (tasks.length === 0) {
                taskList.innerHTML = '<li>No tasks added yet</li>';
            } else {
                tasks.forEach(task => {
                    const taskItem = document.createElement('li');
                    taskItem.classList.add('task-item');
                    if (task.status === 'completa') {
                        taskItem.classList.add('completed');
                    }

                    taskItem.innerHTML = `
                        <span>${task.title}</span>
                        <div>
                            <button class="complete-btn" onclick="completeTask(${task.id})">Complete</button>
                            <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
                        </div>
                    `;

                    taskList.appendChild(taskItem);
                });
            }
        });
}

// Função para adicionar uma nova tarefa
document.getElementById('add-task-btn').addEventListener('click', () => {
    const taskTitle = document.getElementById('task-input').value.trim();

    if (!taskTitle) {
        alert('Task title cannot be empty.');
        return;
    }

    const newTask = {
        title: taskTitle
    };

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newTask)
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById('task-input').value = '';  // Limpa o campo de entrada
        loadTasks();  // Recarrega as tarefas
    });
});

// Função para completar uma tarefa
function completeTask(id) {
    fetch(`${apiUrl}/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status: 'completa' })
    })
    .then(() => loadTasks());  // Recarrega as tarefas
}

// Função para deletar uma tarefa
function deleteTask(id) {
    fetch(`${apiUrl}/${id}`, {
        method: 'DELETE'
    })
    .then(() => loadTasks());  // Recarrega as tarefas
}
