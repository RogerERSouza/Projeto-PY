from dados import pecas
from estoque import listar_pecas

def montar_carro():
    listar_pecas()

    ids = input("IDs das peças: ")
    ids = [int(i.strip()) for i in ids.split(",")]

    for id_escolhido in ids:
        for p in pecas:
            if p.id == id_escolhido:
                if p.estoque > 0:
                    p.estoque -= 1
                    print(f"{p.nome} usada")
                else:
                    print(f"{p.nome} sem estoque")
                break
        else:
            print("ID não encontrado")

    print("Montagem finalizada!\n")