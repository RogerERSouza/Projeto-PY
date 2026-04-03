from datetime import datetime

class Peca:
    def __init__(self, id, nome, custo, preco, estoque, carros, tamanho, localizacao, codigo, fornecedor):
        self.id = id
        self.nome = nome
        self.custo = custo
        self.preco = preco
        self.estoque = estoque
        self.carros = carros
        self.tamanho = tamanho
        self.localizacao = localizacao
        self.codigo_fabricacao = codigo
        self.fornecedor = fornecedor
        self.data_cadastro = datetime.now()