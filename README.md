# Desafio backend iTFLEX Tecnologia

### Objetivo

Criar uma API de um aplicativo de lista de tarefas.

A API deve ter disponibilizar as operações de cadastro de tarefas,
marcar como concluida e excluir tarefas.

### Requisitos

* Desenvolver em Python, NodeJS, PHP ou Ruby
* API deve seguir os princípios REST
* Salvar as informações necessárias em um dos bancos de dados relacionais abaixo:
  * Sqlite
  * PostgreSQL
  * MySQL
* Documentar como rodar o projeto

### Operações desejadas

* Cadastro de tarefas
* Marcar tarefas como concluidas
* Excluir tarefas

### Exemplos de requisições

Requisições e suas respectivas respostas esperadas. Iremos usar estes exemplos para testar sua aplicação.

* Criar uma tarefa:

```
curl -X POST -H "Content-Type: application/json" -d '{"task": "Tomar um café", "done": false}' http://localhost:xxxx/api/tasks
Resposta: HTTP 201
{
  "id": 2,
  "task": "Tomar um café",
  "done": false
}
```

* Lista de tarefas:

```
curl -X GET http://localhost:xxxx/api/tasks
Resposta: HTTP 200
[
  {
    "id": 1,
    "task": "Fazer desafio da iTFLEX",
    "done": false
  },
  {
    "id": 2,
    "task": "Tomar um café",
    "done": true
  }
]
```

* Marcar tarefa como concluida:

```
curl -X PUT -H "Content-Type: application/json" -d '{"done": true}' http://localhost:xxxx/api/tasks/1
Resposta: HTTP 200
{
  "id": 1,
  "task": "Fazer desafio da iTFLEX",
  "done": true
}
```

* Excluir uma tarefa:

```
curl -X DELETE http://localhost:xxxx/tasks/1/
Resposta: HTTP 204
```
