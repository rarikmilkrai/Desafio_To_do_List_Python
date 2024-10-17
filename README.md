# Desafio_To_do_List_Python

Este projeto é uma aplicação de lista de tarefas desenvolvida em Python usando
Flask para o back-end e HTML/CSS/JavaScript para o front-end.
A aplicação permite que os usuários adicionem, completem e excluam tarefas,
armazenando-as de forma persistente.

# Atualmente, o projeto está hospedado em uma instância EC2 da AWS, onde o código foi inserido usando boas práticas de CI/CD.

## Tecnologias Utilizadas

- **Back-end:** Flask (Python)
- **Front-end:** HTML, CSS, JavaScript
- **Banco de Dados:** Redis
- **Testes de API:** Postman

## Configuração do Ambiente

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/rarikmilkrai/Desafio_To_do_List_Python.git
   cd Desafio_To_do_List_Python
   ```

2. **Instale as Dependências do Back-end**

   Navegue até a pasta do back-end e crie um ambiente virtual:

   ```bash
   cd back
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Inicie o Redis**

   Certifique-se de que o Redis está instalado e, em seguida, inicie-o:

   ```bash
   sudo systemctl start redis
   ```

4. **Inicie o Servidor Flask**

   Para iniciar o servidor Flask em segundo plano, use o seguinte comando:

   ```bash
   nohup python todolist_Back.py &
   ```

## Endpoints da API

### Verifique a API com Postman

Você pode verificar a API utilizando o Postman com o seguinte endpoint:

- **API de Tarefas:**
  - URL: `http://54.233.7.48:5000/tasks`

Use este endpoint para fazer solicitações GET, POST, PUT e DELETE para manipular as tarefas.

### Exemplo de JSON para Testes

Incluído no repositório, você encontrará um arquivo JSON que contém uma coleção para testes. Você pode importá-lo para o Postman para facilitar o teste da API.

## Acessando o Front-end

O front-end da aplicação está disponível em:

- **URL do Front-end:**
  - URL: `http://54.233.7.48:8000`

> **Nota:** Atualmente, o front-end está apresentando bugs que podem afetar a funcionalidade de adicionar tarefas. Estamos trabalhando para resolver esses problemas.

Este projeto é de uso livre e está sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.
```

