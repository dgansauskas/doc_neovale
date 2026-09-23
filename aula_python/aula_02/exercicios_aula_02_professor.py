# ==============================================================================
# MODELAGEM, PREPARAÇÃO E ANÁLISE DE DADOS
# AULA 2: EXERCÍCIO PRÁTICO EM SALA DE AULA (GABARITO / RESOLUÇÃO)
# Arquivo: exercicios_aula_02_professor.py
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
        "email": "carlos_email_com",
        "idade": 17,
        "faturamento": "850,00",
        "score_credito": 620
    },
    {
        "id_cliente": 103,
        "nome": "",
        "cpf": "111.222.333-44",
        "email": "mariana@empresa.com.br",
        "idade": 34,
        "faturamento": "R$ -200,00",
        "score_credito": 810
    },
    {
        "id_cliente": 101,
        "nome": "Ana Silva",
        "cpf": "123.456.789-00",
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
        "idade": -5,
        "faturamento": "R$ 3.200,90",
        "score_credito": 450
    }
]


# ==============================================================================
# EXERCÍCIO 1: FUNÇÕES DE SANITIZAÇÃO DE DADOS (RESOLVIDO)
# ==============================================================================

def sanitizar_nome(nome: str) -> str:
    """Remove espaços extras no início/fim e formata em Title Case."""
    if not nome:
        return ""
    return nome.strip().title()


def sanitizar_cpf(cpf: str) -> str:
    """Mantém apenas os dígitos do CPF."""
    if not cpf:
        return ""
    return cpf.replace('.',"").replace('-',"")
    # return re.sub(r"\D", "", cpf) # usando REGEX


def limpar_faturamento(faturamento_raw: str) -> float:
    """Converte texto monetário para valor float."""
    if not faturamento_raw:
        return 0.0
    try:
        texto_limpo = faturamento_raw.replace("R$", "").replace(".", "").replace(",", ".").strip()
        return float(texto_limpo)
    except ValueError:
        return 0.0


# ==============================================================================
# EXERCÍCIO 2: FUNÇÕES DE REGRAS DE NEGÓCIO E DATA QUALITY (RESOLVIDO)
# ==============================================================================

def validar_email(email: str) -> bool:
    """Valida se e-mail possui '@' e '.'."""
    if not email or "@" not in email or "." not in email:
        return False
    return True


def classificar_risco_credito(idade: int, score: int) -> str:
    """Aplica regras de concessão de crédito."""
    if idade < 18:
        return "REPROVADO (Menor de idade)"
    elif score >= 700:
        return "BAIXO RISCO (Aprovado)"
    else:
        return "ALTO RISCO (Análise Manual)"


# ==============================================================================
# EXERCÍCIO 3: PIPELINE DE PROCESSAMENTO E AUDITORIA (RESOLVIDO)
# ==============================================================================

def processar_lote_dados(registros_brutos: list) -> tuple[list, list]:
    """Processa o lote aplicando sanitização e validação de qualidade."""
    dados_saneados = []
    relatorio_erros = []
    ids_visitados = set()

    print("⚡ Executando Pipeline de Dados (Gabarito)...")

    for idx, reg in enumerate(registros_brutos, start=1):
        id_cli = reg.get("id_cliente")
        erros_registro = []

        # 1. Teste de Unicidade
        if id_cli in ids_visitados:
            erros_registro.append(f"UNICIDADE: ID {id_cli} duplicado detectado.")
        else:
            ids_visitados.add(id_cli)

        # 2. Sanitização
        nome_limpo = sanitizar_nome(reg.get("nome", ""))
        cpf_limpo = sanitizar_cpf(reg.get("cpf", ""))
        faturamento_limpo = limpar_faturamento(reg.get("faturamento", ""))

        # 3. Validações de Qualidade
        if not nome_limpo:
            erros_registro.append("COMPLETUDE: Nome está em branco ou ausente.")

        if len(cpf_limpo) != 11:
            erros_registro.append(f"CONFORMIDADE: CPF '{reg.get('cpf')}' inválido (não possui 11 dígitos).")

        if not validar_email(reg.get("email", "")):
            erros_registro.append(f"CONFORMIDADE: E-mail '{reg.get('email')}' é inválido.")

        if reg.get("idade", 0) <= 0:
            erros_registro.append(f"ACURÁCIA: Idade {reg.get('idade')} é inválida.")

        if faturamento_limpo < 0:
            erros_registro.append(f"ACURÁCIA: Faturamento R$ {faturamento_limpo:.2f} não pode ser negativo.")

        # 4. Regra de Negócio
        status_credito = classificar_risco_credito(reg.get("idade", 0), reg.get("score_credito", 0))

        # 5. Registro Final
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
    print("📊 RELATÓRIO DE AUDITORIA E DATA QUALITY (GABARITO)")
    print("=" * 70)
    print(f"Total de registros analisados: {len(dados_brutos)}")
    print(f"Registros com problemas detectados: {len(erros)}")

    if erros:
        print("❌ INCONSISTÊNCIAS ENCONTRADAS:")
        for e in erros:
            print(f"[Linha {e['linha_origem']}] Cliente ID: {e['id_cliente']}")
            for falha in e['falhas']:
                print(f"   └── ⚠️ {falha}")

    print("" + "=" * 70)
    print("✅ DADOS PROCESSADOS:")
    print("=" * 70)
    for cliente in registros_limpos:
        print(cliente)