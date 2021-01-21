from flask import Blueprint, request
from certificado.models.model_group import Group

grupo = Blueprint('group_route', __name__, url_prefix='/group')


""" Recupera todos os grupos """
@grupo.route('/')
def get_all():
    return {'Group': [group.json() for group in Group.query.all()]}


""" Recupera um grupo especifico """
@grupo.route('/<int:id>')
def get(id):
    group = Group.find_group(id)
    if group:
        return group.json()
    return {'mensage': 'Group não existe'}, 404 # Not Found


""" Cadastra um novo Grupo """
@grupo.route('/', methods=['POST'])
def post():
    query = request.json
    group = Group(**query)

    if group.find_group(query['id']):
        return {'mensage': f'O grupo {query["id"]}, já existe'}, 400 # Bad Request
    try:
        group.save_group()
        return {'mensage': 'Group cadastrado com sucesso'}, 200 # OK
    except:
        return {'mensage': 'Erro interno'}, 500 # Internal Error


""" Atualiza/cadastra um grupo """
@grupo.route('/<int:id>', methods=['PUT'])
def put(id):
    query = request.json
    group_encontrado = Group.find_group(id)

    ''' Caso exista o grupo '''
    if group_encontrado:
        group_encontrado.update_group(**query)
        try:
            group_encontrado.save_group()
        except:
            return {'mensage': 'erro ao salvar o group'}, 500  # Internal error
        return group_encontrado.json(), 200 # Success

    ''' Caso não exista o grupo '''
    group = Group(id, **query)
    try:
        group.save_group()
    except:
        return {'mensage': 'Erro ao salvar o group'}, 500 # Internal error
    return group.json(), 200 # Created


""" Apaga um grupo especifico """
@grupo.route('/<int:id>', methods=['DELETE'])
def delete(id):
    group = Group.find_group(id)
    if group:
        group.delete_group()
        return {'mensage': 'group apagado com sucesso!!'}, 200 # Success
    return {'mensage': 'group não encontrado'}, 400 # Not Found