from estoque import cadastrar_peca, listar_pecas, registrar_producao
from vendas import vender_peca, faturamento
from busca import buscar_por_carro
from montagem import montar_carro
# from dados import faturamento

def menu():
    while True:
        print("""
1 - Cadastrar peça
2 - Listar peças
3 - Produção
4 - Vender
5 - Buscar por carro
6 - Montar carro
7 - Ver faturamento
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
        elif op == "7":
            print("Faturamento:", faturamento, "\n")
        elif op == "0":
            break
        else:
            print("Opção inválida!\n")

menu()