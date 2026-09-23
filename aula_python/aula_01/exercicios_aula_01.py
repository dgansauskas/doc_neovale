# ==============================================================================
# EXERCÍCIOS PRÁTICOS DE PYTHON - AULA 01
# Disciplina: Modelagem, Preparação e Análise de Dados
# Instruções: Preencha os campos marcados com '# TODO' para resolver os desafios.
# ==============================================================================

print("=" * 60)
print(" DESAFIO PRÁTICO 1: Validador de Registro Bruto de Cliente")
print("=" * 60)

# Dados brutos recebidos de um sistema legado
nome_bruto = "  Carlos Eduardo  "
idade_input = "34"
valor_compra_input = "450.50"
email_input = "carlos@email.com"

# --- SUAS SOLUÇÕES AQUI ---

# 1. Trate os espaços extras do nome usando .strip()
nome_limpo = None  # TODO: Aplique .strip() em nome_bruto

# 2. Converta idade_input para int e valor_compra_input para float
idade = None       # TODO: Converta idade_input para int
valor_compra = None # TODO: Converta valor_compra_input para float

# 3. Validações
erros = []

# TODO: Se idade for menor que 18, adicione a mensagem "Cliente menor de idade" na lista 'erros'
# TODO: Se email_input não contiver '@', adicione "E-mail inválido" na lista 'erros'

status = "APROVADO" if len(erros) == 0 else "REPROVADO"

print(f"Nome Processado: '{nome_limpo}'")
print(f"Idade (tipo {type(idade).__name__}): {idade}")
print(f"Valor da Compra (tipo {type(valor_compra).__name__}): R$ {valor_compra}")
print(f"Status do Cadastro: {status}")
if erros:
    print(f"Erros encontrados: {erros}")

print("\n" + "=" * 60)
print(" DESAFIO PRÁTICO 2: Normalização de Telefone e Status Ativo")
print("=" * 60)

telefone_bruto = " (11) 99876-5432 "
status_sistema = "TRUE" # Recebido como texto do banco de dados

# --- SUAS SOLUÇÕES AQUI ---

# 1. Remova espaços extras e os caracteres '(', ')', '-' do telefone
# DICA: Você pode encadear o método .replace()
telefone_limpo = None # TODO: Deixe apenas os números no telefone_limpo

# 2. Converta o status_sistema ("TRUE") para um valor booleano nativo (bool)
# DICA: Compare se status_sistema.upper() == "TRUE"
is_ativo = None # TODO: Crie uma expressão booleana (True/False)

print(f"Telefone Sanitizado: {telefone_limpo}")
print(f"Cliente Ativo no Sistema: {is_ativo} (Tipo: {type(is_ativo).__name__})")

print("\n" + "=" * 60)
print(" DESAFIO PRÁTICO 3: Validador de Lote de Vendas (Regras de Negócio)")
print("=" * 60)

qtd_itens_input = "15"
preco_unitario_input = "29.90"
cupom_desconto = "DESCONTO10" # Concede 10% de desconto se for igual a "DESCONTO10"

# --- SUAS SOLUÇÕES AQUI ---

# 1. Converta os tipos de dados apropriados
qtd_itens = None       # TODO: Converta para int
preco_unitario = None  # TODO: Converta para float

# 2. Calcule o valor total bruto
valor_bruto = None     # TODO: qtd_itens * preco_unitario

# 3. Aplique o desconto se o cupom for "DESCONTO10"
taxa_desconto = 0.10 if cupom_desconto == "DESCONTO10" else 0.0
valor_desconto = None  # TODO: valor_bruto * taxa_desconto
valor_final = None     # TODO: valor_bruto - valor_desconto

print(f"Quantidade de Itens: {qtd_itens}")
print(f"Valor Bruto: R$ {valor_bruto:.2f}")
print(f"Desconto Aplicado: R$ {valor_desconto:.2f}")
print(f"Valor Final a Cobrar: R$ {valor_final:.2f}")

print("\n" + "=" * 60)
print(" 🏁 FIM DOS EXERCÍCIOS - VALIDE SEU SAÍDA COM O ESPERADO ABAIXO:")
print("=" * 60)
"""
GABARITO / RESULTADO ESPERADO NO TERMINAL:

DESAFIO PRÁTICO 1:
Nome Processado: 'Carlos Eduardo'
Idade (tipo int): 34
Valor da Compra (tipo float): R$ 450.5
Status do Cadastro: APROVADO

DESAFIO PRÁTICO 2:
Telefone Sanitizado: 11998765432
Cliente Ativo no Sistema: True (Tipo: bool)

DESAFIO PRÁTICO 3:
Quantidade de Itens: 15
Valor Bruto: R$ 448.50
Desconto Aplicado: R$ 44.85
Valor Final a Cobrar: R$ 403.65
"""