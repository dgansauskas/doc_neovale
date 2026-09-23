# ==============================================================================
# MODELAGEM, PREPARAÇÃO E ANÁLISE DE DADOS
# AULA 2: EXERCÍCIO PRÁTICO EM SALA DE AULA (VERSÃO DO ALUNO)
# Arquivo: exercicios_aula_02_aluno.py
# ==============================================================================
# Instruções:
# 1. Complete as funções abaixo substituindo o comando 'pass' pelo seu código.
# 2. Leia atentamente as docstrings e as pistas (HINTS) comentadas.
# 3. Execute o arquivo no seu terminal/VS Code para testar o resultado.
# ==============================================================================

import re

# ------------------------------------------------------------------------------
# BASE DE DADOS BRUTA (Lote de cadastros recebidos com inconsistências)
# ------------------------------------------------------------------------------
dados_brutos = [
    {
        "id_cliente": 101,
        "nome": "  Ana Silva  ",
        "cpf": "123.456.789-00",
        "email": "ana.silva@email.com",
        "idade": 29,
        "faturamento": "R$ 1.500,50",
        "score_credito": 750
    },
    {
        "id_cliente": 102,
        "nome": "Carlos Eduardo",
        "cpf": "98765432100",
        "email": "carlos_email_com",  # E-mail inválido (sem @)
        "idade": 17,                  # Menor de idade
        "faturamento": "850,00",
        "score_credito": 620
    },
    {
        "id_cliente": 103,
        "nome": "",                   # Nome ausente (Completude)
        "cpf": "111.222.333-44",
        "email": "mariana@empresa.com.br",
        "idade": 34,
        "faturamento": "R$ -200,00",  # Valor negativo (Acurácia)
        "score_credito": 810
    },
    {
        "id_cliente": 101,             # ID Duplicado (Unicidade)
        "nome": "Ana Silva",
        "cpf": "123.456.789-00D",
        "email": "ana.silva@email.com",
        "idade": 29,
        "faturamento": "R$ 1.500,50",
        "score_credito": 750
    },
    {
        "id_cliente": 104,
        "nome": "  João Pedro Santos ",
        "cpf": "44455566677",
        "email": "joao.pedro@dominio.org",
        "idade": -5,                  # Idade inválida (Acurácia)
        "faturamento": "R$ 3.200,90",
        "score_credito": 450
    }
]


# ==============================================================================
# EXERCÍCIO 1: FUNÇÕES DE SANITIZAÇÃO DE DADOS
# ==============================================================================

def sanitizar_nome(nome: str) -> str:
    """
    Objetivo: Remover espaços extras no início/fim e formatar o nome em Title Case.
    Exemplo: '  ana silva  ' -> 'Ana Silva'
    """
    # HINT: Se o nome estiver vazio ou None, retorne "".
    # HINT: Use os métodos de string .strip() para remover espaços e .title() para maiúsculas.
    
    # === SUA IMPLEMENTAÇÃO AQUI ===
    if not nome:
        return ""
    return nome.strip().title()


def sanitizar_cpf(cpf: str) -> str:
    """
    Objetivo: Manter apenas os números do CPF (remover pontos, hífens, etc).
    Exemplo: '123.456.789-00' -> '12345678900'
    """
    # HINT: Se cpf for None/vazio, retorne "".
    # HINT: Você pode usar re.sub(r"\D", "", cpf) da biblioteca 're' para remover não-dígitos.
    
    # === SUA IMPLEMENTAÇÃO AQUI ===
    if not cpf:
        return ""
    return cpf.replace(".","").replace("-","")
    # return re.sub(r"\D", "", cpf)


def limpar_faturamento(faturamento_raw: str) -> float:
    """
    Objetivo: Converter texto monetário (ex: 'R$ 1.500,50') em valor float (1500.50).
    """
    # HINT: Se faturamento_raw for vazio, retorne 0.0.
    # HINT: Crie uma sequência de trocas (.replace):
    #   1. Remova 'R$' por ''
    #   2. Remova o ponto '.' por '' (separador de milhar)
    #   3. Troque a vírgula ',' por ponto '.' (separador decimal do Python)
    #   4. Use .strip() para remover espaços e converta com float()
    # HINT: Envolva a conversão em um bloco try/except ValueError para evitar que o código quebre.

    # === SUA IMPLEMENTAÇÃO AQUI ===
    if not faturamento_raw:
        return 0.0
    return float(faturamento_raw
            .replace('R$','')
            .replace('.','')
            .replace(',','.')
            .strip()
    )


# ==============================================================================
# EXERCÍCIO 2: FUNÇÕES DE REGRAS DE NEGÓCIO E DATA QUALITY
# ==============================================================================

def validar_email(email: str) -> bool:
    """
    Objetivo: Verificar se o e-mail possui um formato básico válido.
    Retorna True se for válido, False caso contrário.
    """
    # HINT: Verifique se o e-mail não é vazio, e se contém o caractere '@' E o caractere '.'.
    # HINT: Retorne True se passar na checagem, caso contrário False.

    # === SUA IMPLEMENTAÇÃO AQUI ===
    if not email or '@' not in email or '.' not in email:
        return False
    return True
    


def classificar_risco_credito(idade: int, score: int) -> str:
    """
    Objetivo: Classificar o risco de crédito do cliente baseado em regras:
    - Se idade < 18: 'REPROVADO (Menor de idade)'
    - Se score >= 700: 'BAIXO RISCO (Aprovado)'
    - Caso contrário: 'ALTO RISCO (Análise Manual)'
    """
    # HINT: Use estrutura condicional if / elif / else.

    # === SUA IMPLEMENTAÇÃO AQUI ===
    pass


# ==============================================================================
# EXERCÍCIO 3: PIPELINE DE PROCESSAMENTO E AUDITORIA
# ==============================================================================

def processar_lote_dados(registros_brutos: list) -> tuple[list, list]:
    """
    Objetivo: Percorrer a lista de dicionários brutos, aplicar as funções de limpeza,
    validar regras de Data Quality e gerar o relatório final de auditagem.
    """
    dados_saneados = []
    relatorio_erros = []
    ids_visitados = set()  # Para controle de unicidade de ID

    print("⚡ Executando Pipeline de Testes dos Alunos...")

    for idx, reg in enumerate(registros_brutos, start=1):
        id_cli = reg.get("id_cliente")
        erros_registro = []

        # 1. TESTE DE UNICIDADE (ID Duplicado)
        # HINT: Verifique se id_cli já está em 'ids_visitados'.
        # Se sim, adicione a mensagem "UNICAÇÃO: ID {id_cli} duplicado." na lista erros_registro.
        # Se não, adicione id_cli no conjunto ids_visitados (ids_visitados.add(id_cli)).
        
        # === SUA IMPLEMENTAÇÃO AQUI ===


        # 2. SANITIZAÇÃO (Chamar as funções criadas no Exercício 1)
        # HINT: Passe os valores do dicionário 'reg' para as funções sanitizar_nome, sanitizar_cpf e limpar_faturamento.
        
        nome_limpo = sanitizar_nome(reg.get("nome", ""))
        cpf_limpo = sanitizar_cpf(reg.get("cpf", ""))
        faturamento_limpo = limpar_faturamento(reg.get("faturamento", ""))


        # 3. VALIDAÇÕES DE DATA QUALITY (Checagem de erros)
        # HINT: Teste as seguintes condições e adicione avisos em erros_registro se forem inválidos:
        #   a) Nome limpo está vazio?
        #   b) CPF limpo tem tamanho diferente de 11 dígitos?
        #   c) E-mail é inválido (usando validar_email)?
        #   d) Idade é menor ou igual a 0?
        #   e) Faturamento limpo é menor que 0?

        # === SUA IMPLEMENTAÇÃO AQUI ===


        # 4. APLICAÇÃO DA REGRA DE CRÉDITO
        # HINT: Chame a função classificar_risco_credito passando idade e score_credito.
        status_credito = classificar_risco_credito(reg.get("idade", 0), reg.get("score_credito", 0))


        # 5. CONSTRUÇÃO DO DICIONÁRIO PROCESSADO
        registro_processado = {
            "id_cliente": id_cli,
            "nome": nome_limpo,
            "cpf": cpf_limpo,
            "email": reg.get("email"),
            "idade": reg.get("idade"),
            "faturamento": faturamento_limpo,
            "score_credito": reg.get("score_credito"),
            "status_credito": status_credito,
            "status_qualidade": "APROVADO" if not erros_registro else "COM FALHAS"
        }
        dados_saneados.append(registro_processado)

        # Se houver erros, registra no relatório
        if erros_registro:
            relatorio_erros.append({
                "linha_origem": idx,
                "id_cliente": id_cli,
                "falhas": erros_registro
            })

    return dados_saneados, relatorio_erros


# ==============================================================================
# EXECUÇÃO E TESTE NO TERMINAL
# ==============================================================================

if __name__ == "__main__":
    registros_limpos, erros = processar_lote_dados(dados_brutos)

    print("=" * 70)
    print("📊 RESULTADO DO TESTE DE EXECUÇÃO DO ALUNO")
    print("=" * 70)
    print(f"Total de registros analisados: {len(dados_brutos)}")
    print(f"Registros com problemas detectados: {len(erros)}")

    if erros:
        print("❌ FALHAS IDENTIFICADAS PELO SEU CÓDIGO:")
        for e in erros:
            print(f"[Linha {e['linha_origem']}] Cliente ID: {e['id_cliente']}")
            for falha in e['falhas']:
                print(f"   └── ⚠️ {falha}")
    else:
        print("⚠️ Nenhuma falha detectada! (Verifique se implementou as validações no Exercício 3).")

    print("" + "=" * 70)
    print("✅ AMOSTRA DOS DADOS PROCESSADOS:")
    print("=" * 70)
    for cliente in registros_limpos:
        print(cliente)