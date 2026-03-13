# Sistema de Produção, Vendas e Estoque – PY

## Descrição
Este projeto é um software simples criado para ajudar a empresa **PY**, que produz veículos de corrida, a controlar seus **produtos, produção, vendas e estoque**.

O objetivo é evitar prejuízos e organizar melhor as informações da empresa.

---

## Funcionalidades do Sistema

O sistema permite:

- Cadastrar produtos
- Registrar produção
- Registrar vendas
- Controlar o estoque
- Calcular o faturamento

---

## Dados do Produto

Cada produto possui:

- Nome
- Custo de produção
- Preço de venda
- Quantidade em estoque

---

## Regras de Negócio

### Venda

Ao registrar uma venda:

- O sistema verifica se existe produto no estoque
- Se houver estoque, ele é reduzido
- O valor da venda é somado ao faturamento
- Se não houver estoque, a venda não é realizada

---

## Conceitos Utilizados

O código utiliza:

- **while** → para manter o menu do sistema funcionando  
- **for** → para percorrer a lista de produtos  
- **if / elif** → para decisões no menu e nas vendas  
- **listas** → para armazenar os produtos  

---

## Como Executar

1. Instale o **Python**
2. Execute o arquivo principal:

```bash
python main.py
```
