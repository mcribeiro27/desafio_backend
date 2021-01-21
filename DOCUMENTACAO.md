## Desafio ITFlex

### Apresentação

Documentação para utilização da Doc API - Desafio Backend ITFlex.

## Começando

Para acessar o sistema serão necessários os seguintes programas:

- [Python 3.7.x: necessário para a execução do sistema](https://www.python.org/downloads/)

Foi usado para teste de API o Postman, que pode ser baixado no link abaixo:
- [Postman, usado para teste da API](https://www.postman.com/downloads/)

## Desenvolvimento

Para iniciar, é necessário clonar o projeto do Github em um diretório de sua preferência:

```commandline
cd "diretorio de sua preferencia"
git clone https://github.com/mcribeiro27/desafio_backend
```
## Construção

Para construir o projeto, execute os comandos abaixo dentro da pasta onde baixou o projeto:

Para ambiente Unix/ Mac

```commandline
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Para ambiente Windows

```commandline
pip install virtualenv
virtualenv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```
Depois de tudo configurado execute o comando para criar o banco.
```commandline
flask create-db
```

## Configuração

### Certificados

Está pasta representa um objeto do tipo certificado na Doc Api – Desafio Backend.

### POST


```url
http://127.0.0.1:5000/certificado/
```

Cadastra um novo Certificado no sistema

### Body

```json
{   
    "id": 5,
    "username": "mcribeiro",
    "name": "marcos cesar",
    "description": "123456",
    "expiration": 50,
    "expirated_at": "20/03/2021"
}
```
### Response
```json
{"mensage": "Certificado cadastrado com sucesso"}
```
### GET

```url
http://127.0.0.1:5000/certificado/
```

Lista todos os Certificados do sistema

### Response
```json
{
    "Certificados": [

        {
            "created_at": "Wed, 20 Jan 2021 12:03:24 GMT",
            "description": "123456",
            "expirated_at": "2021-01-20 12:03:24.641879",
            "expiration": 35,
            "groups": [
                {
                    "id": 1,
                    "name": "ADM"
                },
                {
                    "id": 2,
                    "name": "ENG"
                },
                {
                    "id": 11,
                    "name": "ADM"
                }
            ],
            "id": 1,
            "name": "marcos cesar",
            "updated_at": "Wed, 20 Jan 2021 12:03:24 GMT",
            "username": "mcribeiro27"
        },
        {
            "created_at": "Wed, 20 Jan 2021 12:15:07 GMT",
            "description": "123456",
            "expirated_at": "20/03/2021",
            "expiration": 50,
            "groups": [],
            "id": 2,
            "name": "marcos cesar",
            "updated_at": "Wed, 20 Jan 2021 12:15:07 GMT",
            "username": "mcribeiro27"
        }
    ]
}
```
### GET pelo id

```url
http://127.0.0.1:5000/certificado/1
```

Busca pelo id o certificado no sistema
```json
{
    "created_at": "Wed, 20 Jan 2021 12:03:24 GMT",
    "description": "123456",
    "expirated_at": "2021-01-20 12:03:24.641879",
    "expiration": 35,
    "groups": [
            {
                "id": 1,
                "name": "ADM"
            },
            {
                "id": 2,
                "name": "ENG"
            },
            {
                "id": 11,
                "name": "ADM"
            }
    ],
    "id": 1,
    "name": "marcos cesar",
    "updated_at": "Wed, 20 Jan 2021 12:03:24 GMT",
    "username": "mcribeiro27"
}
```

### GET pelo username

```url
http://127.0.0.1:5000/certificado/mcribeiro27
```

Busca pelo id o certificado no sistema
```json
{
    "created_at": "Wed, 20 Jan 2021 12:03:24 GMT",
    "description": "123456",
    "expirated_at": "2021-01-20 12:03:24.641879",
    "expiration": 35,
    "groups": [
            {
                "id": 1,
                "name": "ADM"
            },
            {
                "id": 2,
                "name": "ENG"
            },
            {
                "id": 11,
                "name": "ADM"
            }
    ],
    "id": 1,
    "name": "marcos cesar",
    "updated_at": "Wed, 20 Jan 2021 12:03:24 GMT",
    "username": "mcribeiro27"
}
```

### PUT 

```url
http://127.0.0.1:5000/certificado/<int:id>/
```
Modifica/atualiza um certificado no sistema

### Body

```json
{
    "username": "mcribeiro",
    "name": "marcos cesar",
    "description": "123456",
    "expiration": 50,
    "expirated_at": "20/03/2021"
}
```
### DELETE

```url
http://127.0.0.1:5000/certificado/<int:id>/
```
Deleta um certificado no sistema

### Response
```json
{"mensage": "Certificado apagado com sucesso!!"}
```
### Group

Está pasta representa um objeto do tipo group na Doc Api – Desafio Backend.

### POST

```url
http://127.0.0.1:5000/group/
```
Cadastra um novo group no sistema

### Body

```json
{
    "id": 1,
    "name": "ADM",
    "certificado_id": 1
```
### Response

```json
{"mensage": "Group cadastrado com sucesso"}
```

### GET

```url
http://127.0.0.1:5000/group/
```
Lista todos os group no sistema

### Response

```json
{
    "Group": [
        {
            "id": 1,
            "name": "ADM"
        },
        {
            "id": 2,
            "name": "ENG"
        },
        {
            "id": 11,
            "name": "FIN"
        }
    ]
}
```

### GET por id

```url
http://127.0.0.1:5000/group/<int:id>
```
Busca um group pelo seu id no sistema

### Response

```json
{
    "id": 1,
    "name": "ADM"
}
```
### PUT

```url
http://127.0.0.1:5000/group/<int:id>
```
Modifica/atualiza um group no sistema

### Body

```json
{
    "name": "ADM",
    "certificado_id": 1
}
```
### DELETE

```url
http://127.0.0.1:5000/group/<int:id>
```

Deleta um group no sistema

```json
{"mensage": "Group apagado com sucesso!!"}
```

## Testes

Os testes são executados pelo pytest, para realiza-los primeiramente precisa executar o flask e logo em seguida o pytest.

```commandline
flask run
```
e em um segundo terminal executar:

```commandline
pytest
```