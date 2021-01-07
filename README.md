## Desafioflex

### Objetivo

O desafio é criar uma API para gerenciamento de certificados utilizando o conceito de RESTFULL e deve conter, cadastro, listagem edição e deleção.

### Requisitos

* Nossa stack é desenvolvida em Python 3, porem pode ser feito em NodeJS, PHP ou Ruby
* API deve seguir os princípios REST (Utilizar FLASK é um diferencial)
* Salvar as informações necessárias em um dos bancos de dados relacionais abaixo:
  * Sqlite
  * PostgreSQL
  * MySQL
* Ter cobertura de teste no código (TDD - Utilizar pytest é um diferencial)
* Documentar com README como executar o projeto
* Subir a aplicação em alguma plataforma (Exemplo Heroku)

### Diferencial
* Implementar utilizando `Clean Architecture`
* Utiliza SQLAlchemy na camada de banco
* Utiliza sql-migrate para construir banco

### Plus
* `groups` o objetivo deste campo é organiza os certificados em grupos.
  O certificado pode pertencer a mais de um grupo.
  Este campo recebe uma lista de interios, pre-definidos:
    - `01`: Adm
    - `15`: Comercial
    - `30`: RH
* Na listagem permitir ordena pelos campos `username` e `name`
* Na listagem permitir filtra pelos campos `username` e `name`

### Campos

```
{
  "id": 1,
  "username": "joaos", //obrigatório e único, permitindo caracteres `a-z` e `0-9` e máximo de caracteres deve ser 30
  "name": "João da Silva", //obrigatório e máximo de caracteres deve ser 255
  "description": "",
  "groups": [15],
  "expiration" 10, //representa o número de dias que o certificado é valido, o número deve estar entre 10 e 3650.
  "expirated_at": "2020-10-21T13:45:11-03:00", //preenche com a data calculda com base no valor informado no campo expiration, não é cadastrado e nem editado
  "created_at": "2020-10-21T13:45:11-03:00", //preenche com a data atual quando esta criando o certificado
  "updated_at": "2020-10-21T13:45:11-03:00" //preenche com a data atual quando esta modificando o certificado
}
```
