# Checklist de Requisitos — `cadastrar.py`

> ETAPA 1 - CADASTRO DE PEÇAS 

---

## ✅ Implementado

| # | Requisito | Onde no código |
|---|-----------|----------------|
| 1 | **Usar `datetime`** | `datetime.now()` salvo em `self.data_cadastro` na classe `Peca` |
| 2 | **ID de cadastro das peças** | Gerado automaticamente com `len(pecas) + 1` |
| 3 | **Cadastro para mais de um veículo** | Campo `carros` aceita lista separada por vírgula e converte com `.split(",")` |
| 4 | **Código de fabricação** | Campo `codigo_fabricacao` existe na classe e é coletado em `cadastrar_peca()` |
| 5 | **Fornecedor** | Campo `fornecedor` existe na classe e é coletado em `cadastrar_peca()` |
| 6 | **Mostrar quem tirou a peça (matrícula)** | Matrícula coletada e impressa em `registrar_producao()` e `vender_peca()` |

---

## ❌ Incompleto / Inexistente

### 1. `listar_pecas()` — **função não definida**
- É chamada em **3 lugares** do código (menu, `registrar_producao()`, `vender_peca()`)
- O programa **quebra imediatamente** ao tentar usar qualquer uma dessas opções
- **O que falta:** definir a função que percorre a lista `pecas` e exibe os dados de cada peça

---

### 2. `buscar_por_carro()` — **função não implementada**
- Aparece no menu (opção `5`) mas o corpo da função **não existe**
- **O que falta:** receber o nome de um carro (ex: `"Fusca"`), filtrar as peças pelo campo `carros` e exibir somente as compatíveis
- O `pecas.json` já tem essa estrutura pronta no campo `veiculos`

---

### 3. `montar_carro()` — **função não implementada**
- Aparece no menu (opção `6`) mas o corpo da função **não existe**
- **O que falta:**
  - Pedir o modelo do carro
  - Listar as peças necessárias para aquele modelo
  - Verificar se o estoque de cada peça é suficiente
  - Subtrair `1` unidade de cada peça do estoque ao montar

---

### 4. Separação por localização no almoxarifado — **sem agrupamento**
- Os campos `tamanho`, `preco` e `localizacao` existem na classe `Peca`
- **O que falta:** uma função que agrupe e exiba as peças organizadas por `localizacao`, mostrando `tamanho` e `preco` lado a lado

---

### 5. Integração com `pecas.json` — **arquivo nunca é lido nem salvo**
- O arquivo `pecas.json` contém **100 peças** já cadastradas
- O código **nunca carrega** esse arquivo ao iniciar
- O código **nunca salva** alterações (cadastros, vendas, produções)
- Tudo que é feito em memória **se perde ao fechar o programa**
- **O que falta:** usar `json.load()` na inicialização e `json.dump()` após cada alteração

---

## Resumo

```
Total de requisitos:   11
✅ Implementados:       6
❌ Faltando:            5
```

> **Prioridade de implementação sugerida:**
> 1. `listar_pecas()` — o programa não funciona sem ela
> 2. Integração com `pecas.json` — sem isso os dados não persistem
> 3. `buscar_por_carro()`
> 4. `montar_carro()`
> 5. Agrupamento por localização no almoxarifado