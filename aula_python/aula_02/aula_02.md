---
marp: true
theme: uncover
class: invert
paginate: true
size: 16:9
header: "Modelagem & Preparação de Dados | Aula 2"
footer: "Estruturas de Dados, Funções e Qualidade de Dados"
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 60px 40px 30px 40px !important; /* Margem superior padronizada */
    font-size: 22px;
    text-align: left;
    justify-content: flex-start !important; /* Todos os slides começam no topo */
  }
  section.bg-white {
    background-color: #eeebeb !important;
    color: #1e1e1e !important;
  }
  section.bg-white h1, section.bg-white h2 {
    color: #245d8b !important;
  }
  section.bg-white h3, section.bg-white h4 {
    color: #3776AB !important;
  }
  section.bg-white p, section.bg-white li {
    color: #222222 !important;
  }
  h1 {
    color: #FFD43B;
    font-size: 1.7em;
    margin-top: 0;
  }
  h2 {
    color: #FFD43B;
    font-size: 1.4em;
    margin-top: 0;
  }
  h3 {
    color: #4B8BBE;
    font-size: 1.2em;
    margin-top: 5px;
  }
  h4 {
    color: #4B8BBE;
    font-size: 1.0em;
  }
  strong {
    color: #64B5F6;
  }
  code {
    background-color: #1e1e1e;
    color: #FFD43B;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.85em;
  }
  pre {
    background-color: #1e1e1e;
    padding: 10px 12px;
    border-radius: 6px;
    font-size: 0.72em !important; /* Fonte menor para não estourar a página */
    line-height: 1.25;
    white-space: pre-wrap !important; /* Quebra linhas longas no PDF */
    word-break: break-word;
    page-break-inside: avoid;
    overflow: hidden;
  }
  table {
    font-size: 0.8em;
    margin-top: 10px;
  }
  th {
    background-color: #245d8b;
    color: #ffffff;
  }
  blockquote {
    background: #1e1e1e;
    border-left: 4px solid #FFD43B;
    padding: 8px 12px;
    font-size: 0.85em;
  }

---

# 🐍 Aula 2: Estruturas de Dados, Funções & Qualidade

### Modelagem, Preparação e Análise de Dados
**Foco de hoje:** Trabalhar com múltiplos dados em memória, criar código reutilizável e introduzir conceitos de qualidade de dados.

**Danilo Gansauskas**

---

## 🎯 Objetivos da Aula de Hoje

1. **Coleções em Python:** Entender e manipular Listas, Dicionários e Tuplas.
2. **Laços de Repetição:** Iterar sobre conjuntos de dados com `for` e `while`.
3. **Modularização:** Criar funções customizadas (`def`) com boas práticas de código limpo.
4. **Qualidade de Dados:** Compreender a importância de validações, esquemas e dicionários de dados no pipeline.
5. **Prática:** Criar um script de limpeza e padronização de registros brutos em Python puro.

---

## 📦 Coleções em Python: Como Organizar Dados?

Na Aula 1 vimos variáveis soltas (`nome`, `idade`). No mundo real de dados, trabalhamos com **conjuntos de informações**.

* **Lista (`list`):** Coleção **ordenada e mutável**. Aceita duplicatas.
* **Dicionário (`dict`):** Estrutura de **Chave-Valor**. Perfeito para representar uma linha ou registro de uma tabela.
* **Tupla (`tuple`):** Coleção **ordenada e imutável** (valores constantes).

---

## 📜 Listas (`list`)

Utilizadas para armazenar sequências de itens.

```python
# Criando uma lista de cidades
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba"]

# Acessando por índice (inicia em 0)
print(cidades[0])  # 'São Paulo'

# Adicionando e removendo elementos
cidades.append("Belo Horizonte")
cidades.remove("Rio de Janeiro")

print(len(cidades))  # Tamanho da lista: 3
```

---

## 🔑 Dicionários (`dict`)

A estrutura mais importante para simular **registros e tabelas** em Python puro antes de usar o Pandas.

```python
# Representando um cliente (Registro)
cliente = {
	"id": 101,
	"nome": "Ana Silva",
	"idade": 29,
	"email": "ana.silva@email.com",
	"ativo": True
}

# Acessando e alterando valores
print(cliente["nome"])  # 'Ana Silva'
cliente["idade"] = 30    # Atualizando a idade
```

---

## 🔄 Laços de Repetição: Percorrendo Dados

O laço `for` é a ferramenta principal para varrer coleções e aplicar transformações item por item.

```python
# Lista de registros (Tabela em memória)
clientes = [
	{"nome": "Carlos", "compra": 150.0},
	{"nome": "Mariana", "compra": 320.5},
	{"nome": "João", "compra": 90.0}
]

# Iterando e somando os valores
total_vendas = 0
for item in clientes:
	total_vendas += item["compra"]

print(f"Total Vendido: R$ {total_vendas:.2f}")
```

---

## 🛠️ Modularização com Funções (`def`)


Funções evitam repetição de código (**DRY - Don't Repeat Yourself**) e criam **regras reutilizáveis** para o pipeline de dados.

### Exemplo 1: Limpeza de Valores Financeiros
Dados brutos de Vendas costumam vir formatados como texto: `"R$ 1.250,50"`.

```python
def limpar_valor_monetario(valor_texto: str) -> float:
	"""Remove símbolos da moeda e converte para número decimal (float)."""
	texto_limpo = valor_texto.replace("R$", "").replace(".", "").replace(",", ".").strip()
	return float(texto_limpo)

# Aplicando a função em diferentes registros recebidos:
preco_venda1 = limpar_valor_monetario("R$ 1.500,00")  # Retorna: 1500.0
preco_venda2 = limpar_valor_monetario("  R$ 89,90  ")  # Retorna: 89.9

print(preco_venda1 + preco_venda2)  # 1589.9 (Soma matemática direta!)
```

---
## 🛠️ Funções no Mundo Real: Regras de Negócio

### Exemplo 2: Classificação do Status do Cliente
Automatizando a tomada de decisão para cada linha da base de dados.

```python
def classificar_risco_credito(idade: int, score: int) -> str:
	"""Retorna a categoria de risco baseada no perfil financeiro."""
	if idade < 18:
		return "REPROVADO (Menor de idade)"
	elif score >= 700:
		return "BAIXO RISCO"
	else:
		return "ALTO RISCO"

# Reutilizando a mesma regra para vários clientes:
print(classificar_risco_credito(idade=25, score=820)) # BAIXO RISCO
print(classificar_risco_credito(idade=17, score=900)) # REPROVADO (Menor de idade)
print(classificar_risco_credito(idade=40, score=550)) # ALTO RISCO
```

---

## 🛡️ O que é Qualidade de Dados (Data Quality)?

Dados ruins geram análises incorretas e quebram relatórios corporativos (*"Garbage In, Garbage Out"*).

### As 4 Dimensões Básicas da Qualidade:
1. **Completude:** O dado está ausente ou nulo quando deveria existir?
2. **Conformidade:** O formato segue o padrão estipulado? (ex: CPF com 11 dígitos, e-mail com `@`).
3. **Unicidade:** Existem registros duplicados na base?
4. **Acurácia:** O valor faz sentido no mundo real? (ex: idade negativa, valor de venda zero).

---

## 📖 O que é um Dicionário de Dados?

É a **documentação técnica** que especifica o significado, tipo e regras de cada campo de uma tabela.

| Campo | Tipo | Descrição | Regra de Validação |
| :--- | :--- | :--- | :--- |
| `id_cliente` | `int` | Identificador único | Obrigatório, chave primária |
| `nome` | `string` | Nome completo | Mínimo 3 caracteres, sem espaços nas pontas |
| `cpf` | `string` | CPF sanitizado | Exatamente 11 dígitos numéricos |
| `valor` | `float` | Valor da transação | Deve ser maior que 0 |

---

## 💻 Mão na Massa: Exercício Prático em Sala

### 📂 Arquivo de Trabalho: `aula2_pratica.py`

**Desafio:** Construir um pipeline de saneamento em Python que receba uma lista de dicionários brutos do sistema legado e entregue um relatório limpo e validado.

1. Abra o VS Code com o ambiente `.venv` ativado.
2. Crie o arquivo `aula2_pratica.py`.
3. Implemente as funções de validação e processe o lote de dados.

⏱️ **Tempo estimado:** 1 hora e 30 minutos

---

## 🏁 Próxima Aula: Modelagem de Dados

* Conceitos de **OLTP vs. OLAP** (Modelagem Relacional vs. Dimensional).
* **Star Schema** e **Snowflake Schema** (Fatos e Dimensões).