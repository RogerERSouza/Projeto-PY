import json
import os

pecas = []
faturamento = 0

caminho_json = os.path.join(os.path.dirname(__file__), "..", "pecas.json")

def carregar_json():
    """Carrega as peças do arquivo JSON"""
    global pecas
    try:
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo pecas.json não encontrado!")

def salvar_json():
    """Salva as peças no arquivo JSON"""
    try:
        pecas_dict = []
        for p in pecas:
            pecas_dict.append({
                "id": p.id,
                "peca": p.nome,
                "tipo": getattr(p, "tipo", ""),
                "parte": getattr(p, "parte", ""),
                "veiculos": p.carros,
                "fabricante": p.fornecedor,
                "data_fabricacao": p.data_cadastro.strftime("%Y-%m-%d") if hasattr(p, "data_cadastro") else ""
            })
        
        dados = {"pecas": pecas_dict}
        
        with open(caminho_json, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print("Dados salvos no JSON!\n")
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}\n")
