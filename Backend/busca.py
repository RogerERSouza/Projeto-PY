from dados import pecas

def buscar_por_carro():
    carro = input("Carro: ").lower()

    resultados = []

    for p in pecas:
        for c in p.carros:
            if carro == c.lower():
                resultados.append(p)

    if not resultados:
        print("Nenhuma peça encontrada.\n")
        return

    for p in resultados:
        print(f"{p.id} - {p.nome} (Estoque: {p.estoque})")
    print()