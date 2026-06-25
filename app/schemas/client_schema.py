from marshmallow import Schema, fields, validate, ValidationError

class ClientCreateSchema(Schema):
    """Schema para a criação de cliente"""
    nome = fields.String(required=True, validate=validate.Length(min=2, max=120))
    cpf = fields.String(required=True)
    rg = fields.String(required=True)
    telefone = fields.String(required=True)
    email = fields.Email(required=True)
    numero = fields.String()
    logradouro = fields.String()
    bairro = fields.String()
    cidade = fields.String()
    estado = fields.String()
    cep = fields.String()
    data_nascimento = fields.Date(format="%Y-%m-%d")

class ClientUpdateSchema(Schema):
    """Schema para a atualizar de cliente"""
    nome = fields.String(validate=validate.Length(min=2, max=120))
    cpf = fields.String()
    rg = fields.String()
    telefone = fields.String()
    email = fields.Email()
    numero = fields.String()
    logradouro = fields.String()
    bairro = fields.String()
    cidade = fields.String()
    estado = fields.String()
    cep = fields.String()
    data_nascimento = fields.Date(format="%Y-%m-%d")

class ClientResponseSchema(Schema):
    """Schema para a mostrar de cliente"""
    id = fields.String()
    nome = fields.String(validate=validate.Length(min=2, max=120))
    cpf = fields.String()
    rg = fields.String()
    telefone = fields.String()
    email = fields.Email()
    numero = fields.String()
    logradouro = fields.String()
    bairro = fields.String()
    cidade = fields.String()
    estado = fields.String()
    cep = fields.String()
    data_nascimento = fields.Date(format="%Y-%m-%d")
    created_at = fields.DateTime(format="%Y-%m-%d %H:%M:%S")


client_create_schema = ClientCreateSchema()
client_update_schema = ClientUpdateSchema()
client_response_schema = ClientResponseSchema()
client_response_schema = ClientResponseSchema(many=True)