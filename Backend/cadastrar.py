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

pecas = []

def cadastrar_peca():
    nome = input("Nome: ")
    custo = float(input("Custo: "))
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    carros = input("Carros compatíveis (separados por vírgula): ").split(",")
    tamanho = input("Tamanho: ")
    localizacao = input("Localização no estoque: ")
    codigo = input("Código de fabricação: ")
    fornecedor = input("Fornecedor: ")

    nova_peca = Peca(
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

    pecas.append(nova_peca)
    print("Peça cadastrada com sucesso!\n")

def registrar_producao():
    listar_pecas()
    id_digitado = int(input("Id da peça: "))
    matricula = input("Matrícula do funcionário: ")

    for p in pecas:
        if p.id == id_digitado:
            valor = int(input("Quantidade a adicionar: "))
            p.estoque += valor
            print("Novo estoque:", p.estoque)
            print("Alterado por:", matricula)
            print("Data:", datetime.now(), "\n")
            return

    print("Peça não encontrada!\n")

def vender_peca():
    listar_pecas()
    id_digitado = int(input("Id da peça: "))
    matricula = input("Matrícula do funcionário: ")

    for p in pecas:
        if p.id == id_digitado:
            quantidade = int(input("Quantidade a vender: "))
            if quantidade > p.estoque:
                print("Estoque insuficiente!\n")
            else:
                p.estoque -= quantidade
                print("Novo estoque:", p.estoque)
                print("Alterado por:", matricula)
                print("Data:", datetime.now(), "\n")
            return

    print("Peça não encontrada!\n")


def menu():
    while True:
        print("""
1 - Cadastrar peça
2 - Listar peças
3 - Registrar produção (entrada)
4 - Vender peça (saída)
5 - Buscar peças por carro
6 - Montar carro
0 - Sair
""")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_peca()
        elif op == "2":
            listar_pecas()
        elif op == "3":
            registrar_producao()
        elif op == "4":
            vender_peca()
        elif op == "5":
            buscar_por_carro()
        elif op == "6":
            montar_carro()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

menu()
