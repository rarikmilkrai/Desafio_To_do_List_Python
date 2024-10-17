# Documentação do Código Flask - Gerenciamento de Tarefas

## Descrição Geral

Este código implementa uma API de gerenciamento de tarefas (To-Do List) utilizando o framework Flask. A API permite criar, listar, atualizar e excluir tarefas, além de utilizar Redis para cache e SQLite para persistência de dados.

### Estrutura do Código

1. **Bibliotecas Utilizadas:**
   - **Flask:** Framework web utilizado para criar a API.
   - **Flask_SQLAlchemy:** Extensão do Flask para facilitar a interação com bancos de dados SQL.
   - **Redis:** Utilizado para armazenar o cache das tarefas e melhorar o desempenho das requisições.
   - **Flask_CORS:** Extensão que permite requisições de diferentes domínios (CORS - Cross-Origin Resource Sharing).

2. **Configuração da Aplicação:**
   - O Flask é configurado com o SQLite como banco de dados, armazenando as informações das tarefas em um arquivo `tasks.db`.
   - O Redis é configurado para rodar localmente e é utilizado para cachear as tarefas, acelerando a resposta em leituras subsequentes.

3. **Modelo de Dados (Task):**
   - A classe `Task` é o modelo que define a estrutura da tabela no banco de dados, onde cada tarefa contém:
     - `id`: Identificador único da tarefa.
     - `title`: Título da tarefa (obrigatório).
     - `status`: Status da tarefa, que pode ser 'pendente' por padrão ou atualizado pelo usuário.

4. **Rotas Disponíveis na API:**
   - **GET /tasks**: Retorna a lista de tarefas. Se as tarefas estiverem em cache (Redis), elas são retornadas diretamente de lá para melhorar a performance.
   - **POST /tasks**: Adiciona uma nova tarefa. O título da tarefa é obrigatório e validado antes da inserção. Após a inserção, o cache de tarefas é invalidado (deletado do Redis).
   - **PUT /tasks/<int:id>**: Atualiza o status de uma tarefa específica com base em seu ID. Se a tarefa não for encontrada, a API retorna um erro.
   - **DELETE /tasks/<int:id>**: Exclui uma tarefa específica com base em seu ID. Similar à rota PUT, retorna um erro se a tarefa não for encontrada.

5. **Validação de Dados:**
   - O código inclui uma função `validate_task_data` que valida se o campo `title` está presente e não está vazio ao tentar adicionar uma nova tarefa.

6. **Integração com Redis:**
   - Redis é utilizado como um cache para armazenar as tarefas retornadas pela rota GET `/tasks`. Ao adicionar, atualizar ou deletar uma tarefa, o cache é invalidado para garantir que a próxima consulta retorne as informações corretas do banco de dados.

7. **Banco de Dados:**
   - SQLite é utilizado para persistência de dados das tarefas. O banco de dados é criado automaticamente ao inicializar o servidor Flask se ele não existir.

8. **Execução do Servidor:**
   - O servidor Flask é iniciado com o comando `app.run()` e está configurado para rodar na porta 5000, aceitando conexões de qualquer endereço IP (`0.0.0.0`). O modo de depuração (`debug=True`) está ativado para facilitar o desenvolvimento.
