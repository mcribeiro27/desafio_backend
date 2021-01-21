from flask import Blueprint, request
from certificado.models.model_certificado import Certificado


certificado = Blueprint('certificado_routes', __name__, url_prefix='/certificado')


''' Recupera todos os certificados '''
@certificado.route('/')
def get_all():
    return {'Certificados': [certificado.json() for certificado in Certificado.query.all()]}


''' Recupera um certificado especifico '''
@certificado.route('/<int:id>')
def get(id):
    certificado = Certificado.find_certificado(id)
    if certificado:
        return certificado.json()
    return {'mensage': 'Certificado não existe'}, 404 # Not Found


''' Recupera um certificado especifico pelo username'''
@certificado.route('/<username>')
def get_username(username):
    certificado = Certificado.find_username(username)
    if certificado:
        return certificado.json()
    return {'mensage': 'Certificado não existe'}, 404 # Not Found


''' Cadastra um novo certificado '''
@certificado.route('/', methods = ['POST'])
def post():
    query = request.json
    certificado = Certificado(**query)
    if Certificado.find_certificado(query['id']):
        return {'mensage': f'Certificado {query["id"]} já existe'}, 400 # bad request
    try:
        certificado.save_certificado()
        return {'mensage': 'Certificado cadastrado com sucesso'}, 200 # Ok
    except:
        return {'mensage': 'Internal error'}, 500 # Internal Error


''' Atualiza um certificado '''
@certificado.route('/<int:id>', methods=['PUT'])
def put(id):
    query = request.json
    certificado_encontrado = Certificado.find_certificado(id)

    ''' caso exista o certificado '''
    if certificado_encontrado:
        certificado_encontrado.update_certificado(**query)
        try:
            certificado_encontrado.save_certificado()
        except:
            return {'mensage': 'Erro ao salvar o certificado'}, 500 # Internal Error
        return certificado_encontrado.json(), 200 # Success

    ''' caso o certificado não exista '''
    certificado = Certificado(id, **query)
    try:
        certificado.save_certificado()
    except:
        return {'mensage': 'Erro ao salvar o certificado'}, 500 # Internal Error
    return certificado.json(), 201 # Created


""" Apaga o certificado selecionado """
@certificado.route('/<int:id>', methods=['DELETE'])
def delete(id):
    certificado = Certificado.find_certificado(id)
    if certificado:
        certificado.delete_certificado()
        return {'mensage': 'certificado apagado'}, 200 # Success
    return {'mensage': 'certificado não encontrado'}, 404 # Not Found