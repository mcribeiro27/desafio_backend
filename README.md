# Vaga desenvolvedor backend iTFLEX Tecnologia

## Descrição

Oportunidades para vagas de desenvolvedor Backend, para desenvolvimento de interface de administração e geração de relatórios de servidores de telefonia IP e firewall, além de serviços de processamento de dados, e APIs de controle e integração com terceiros.

Trabalho presencial em Joinville / SC

Empresa com 13 anos de mercado, contato com novas tecnologias, oferece possibilidade de crescimento profissional.

Localizada em Joinville, a maior cidade de Santa Catarina (500 mil habitantes), próximo a diversas praias (até 100Km), e também a capital Florianópolis (180Km) e a capital do Paraná, Curitiba (130Km).

A empresa trabalha com as seguintes tecnologias:

* python
* MongoDB
* RabbitMQ
* Docker
* Nginx
* Arquitetura de microsserviços
* JWT
* APIs REST

## Benefícios

* Benefícios CLT + Plano de Saúde + Ticket Refeição + Auxílio Faculdade / Pós Graduação
* Sala de descompressão com vídeo game
* Bons equipamentos para trabalho, uso de dois monitores.
* Máquina de café expresso
* Participação em congressos
* Livros e ebooks para estudo
* Utlização da metologia Scrum

## Perfil

* Gostar muito desenvolvimento de software e tecnologia
* Ser participativo na construção do produto, contribuindo com ideias para o negócio
* Ser dinâmico e inquieto, questionando dogmas e premissas, sempre procurando inovação
* Ter facilidade de trabalhar dentro de times multi-disciplinares
* Ter iniciativa para estudos
* Acompanhar tendências e inovações que surgem no mercado
* Ser poliglota em linguagens de programação e scripting
* Escrever código limpo e legível para pessoas
* Ter profunda preocupação com qualidade e performance
* Compreender a importância e praticar versionamento de código
* Ter conhecimentos em design e arquitetura de software

## Requisitos

* Curso superior em andamento ou concluído em Sistemas de Informação, Ciências da Computação ou Engenharia da computação
* Ter experiência com a linguagem de programação Python
* Entender o funcionamento do protocolo HTTP
* Ter experiência com bibliotecas e frameworks web backend (Flask, Django, Bottle, etc)
* Ter experiência na aplicação de banco de dados no desenvolvimento de sistemas
* Entender os conceitos de modelagem de banco de dados

## Diferenciais

* Ter experiência em utilização do Git
* Conhecer/utilizar expressões regulares
* Ter experiência com métodos ágeis (Scrum, Kanban, Lean, etc)
* Ter conhecimento/experiência na utilização de TDD
* Experiência com bancos de dados NoSQL orientado a documentos (MongoDB, CouchDB, RethinkDB, etc)
* Utilizar/conhecer o banco de dados SQL (MySQL, PostgreSQL, etc)
* Usar/conhecer Linux
* Ter conhecimentos na linguagem de scripts Bash

Tratamos todas as nossas aplicações como sistemas de missão crítica.

Usamos software livre na grande maioria das aplicações e ferramentas por trás do nosso sistema.

## Desafios

Para se candidatar a vaga, resolve os desafios abaixo e envie os repositórios com as respostas
por email para a iTFLEX.

### Desafio 1

Você faz parte de um esquadrão anti-bombas, e um terrorista
armou uma bomba que só pode ser desarmada se resolver o desafio que ele criou.

O desafio é o seguinte:

Existe quatro botões, um vermelho, um azul, um verde e um amarelo.
Um destes botões desarma a bomba, mas você precisa descobrir qual.

Para cada botão, foi associado um código:

| Cor      | Código            |
| -------- | ----------------- |
| VERMELHO | IAJNLITLUNAYDHFAA |
| AZUL     | EFDLUMHBNDRRTM    |
| VERDE    | ZTRAHDSICFQH      |
| AMARELO  | QPSKXDLPWFLAAKHY  |

Para resolver este desafio, foi associado um valor númerico para cada letra,
sendo 1 para A até 26 para Z.

O desafio é descobrir a soma dos valores das letras de cada código e cor,
depois fazer a divisão do valor descoberto de cada código pelo valor descoberto da cor,
onde o resto desta divisão deve ser 11.

O botão que encaixar nesta resolução desarma a bomba.

Enviar a resposta deste desafio juntamente com o link para o repositório com a resolução
do desafio 2.

### Desafio 2

#### Objetivo

Criar uma API de um aplicativo de lista de tarefas.

A API deve ter disponibilizar as operações de cadastro de tarefas,
marcar como concluida e excluir tarefas.

#### Requisitos

* Desenvolver em Python, NodeJS, PHP ou Ruby
* API deve seguir os princípios REST
* Salvar as informações necessárias em um dos bancos de dados relacionais abaixo:
  * Sqlite
  * PostgreSQL
  * MySQL
* Documentar como rodar o projeto

#### Operações desejadas

* Cadastro de tarefas
* Marcar tarefas como concluidas
* Excluir tarefas

#### Exemplos de requisições

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
