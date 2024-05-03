# API

Esta API foi desenvolvida utilizando o framework Django com o DjangoREST. 
Está hospedada na plataforma Render e pode ser acessada através do seguinte endereço: [https://api-axis.onrender.com](https://api-axis.onrender.com).
O banco de dados utilizado é o PostgreSQL, também hospedado na Render.



# DOCUMENTAÇÃO

## Método: GET
Endpoint: https://api-axis.onrender.com/data
Descrição: Retorna detalhes de um produto específico.
Parâmetros:
```json
{
    "id": ID,
    "produto": STRING,
    "quantidade": INT,
    "preco": DECIMAL,
    "descricao": STRING
}
```

## Método: POST
Endpoint: https://api-axis.onrender.com/produtos/
Descrição: Cria um novo produto.
Corpo da Solicitação:
```json
{
    "produto": STRING,
    "quantidade": INT,
    "preco": DECIMAL,
    "descricao": STRING
}
```
Resposta de Sucesso: Status 201 Created

## Método: PUT
Endpoint: https://api-axis.onrender.com/produtos/{id}/
Descrição: Atualiza os detalhes de um produto existente.
Parâmetros:
```json
{
    "id": ID,
    "produto": STRING,
    "quantidade": INT,
    "preco": DECIMAL,
    "descricao": STRING
}
```
Resposta de Sucesso: Status 200 OK

## Método: DELETE
Endpoint: https://api-axis.onrender.com/produtos/{id}/
Descrição: Exclui um produto existente.
Parâmetros:
```json
{
    "id": ID,
}
```
Resposta de Sucesso: Status 204 No Content

