from dados import pecas, faturamento
from estoque import listar_pecas
from datetime import datetime

def vender_peca():
    global faturamento

    listar_pecas()
    id_digitado = int(input("ID: "))
    matricula = input("Matrícula: ")

    for p in pecas:
        if p.id == id_digitado:
            qtd = int(input("Quantidade: "))

            if qtd > p.estoque:
                print("Estoque insuficiente!\n")
            else:
                p.estoque -= qtd
                total = qtd * p.preco
                faturamento += total

                print("Venda realizada!")
                print("Total:", total)
                print("Faturamento:", faturamento)
                print("Data:", datetime.now(), "\n")
            return

    print("Peça não encontrada!\n")