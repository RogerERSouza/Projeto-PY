from models import Peca
from dados import pecas
from datetime import datetime

def cadastrar_peca():
    nome = input("Nome: ")
    custo = float(input("Custo: "))
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    carros = input("Carros (separados por vírgula): ").split(",")
    tamanho = input("Tamanho: ")
    localizacao = input("Localização: ")
    codigo = input("Código: ")
    fornecedor = input("Fornecedor: ")

    nova = Peca(
        id=len(pecas) + 1,
        nome=nome,
        custo=custo,
        preco=preco,
        estoque=estoque,
        carros=[c.strip() for c in carros],
        tamanho=tamanho,
        localizacao=localizacao,
        codigo=codigo,
        fornecedor=fornecedor
    )

    pecas.append(nova)
    print("Peça cadastrada!\n")


def listar_pecas():
    if not pecas:
        print("Nenhuma peça cadastrada.\n")
        return

    for p in pecas:
        print(f"{p.id} - {p.nome} | Estoque: {p.estoque}")


def registrar_producao():
    listar_pecas()
    id_digitado = int(input("ID: "))
    matricula = input("Matrícula: ")

    for p in pecas:
        if p.id == id_digitado:
            qtd = int(input("Quantidade: "))
            p.estoque += qtd
            print("Novo estoque:", p.estoque)
            print("Funcionário:", matricula)
            print("Data:", datetime.now(), "\n")
            return

    print("Peça não encontrada!\n")