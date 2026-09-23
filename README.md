# Documentação do Projeto - Neovale

## Visão Geral
Este documento servecomo padrão para registrar o desenvolvimento dos alunos Neovale.

---

## 1. Sobre o Projeto

- ***Nome do Projeto:*** Neovale
- **Descrição:** O projeto visa que o aluno Neovale crie pilares de competências para conseguir atuar em um ambiente de tecnologia.

---

## 2. Tratamento de Dados
- O tratamento de dados envolve a estruturação e limpeza de bases para garantir análises consistentes.
- No ecossistema dos projetos, contempla desde a modelagem de tabelas relacionais até a engenharia de dados aplicada.

---

## 3. SQL (Structured Query Language)
- Essencial para adminiatração de bancos de dados relacionais e extração de métricas analíticas.
- Utilizado para consultas corporativas e estruturação de tabelas do tipo fato e dimensão e emulamos também o modelo de camadas medalhão(bronze, prata e ouro).

Exemplo de uma consulta na tabela **`fato_vendas`**
```sql
SELECT  cliente_id, SUM(valor)
FROM fato_vendas
WHERE status = 'APROVADO'
GROUP BY cliente_id 
```
---

## 4. Python 🐍
- Linguagem principal para manipulação de dados (inclusive Big Data), automação de tarefas, construção de scripts e desenvolvimento de APIs robustas com `FastAPI`.
- Utiliza ecossistemas modernos de desenvolvimento e dependencias gerenciadas por ferramentas como o `pip` e `poetry`.

```python
# Exemplo de processamento analítico básico
resultado = 10 + 20
print(f"Resultado final do processamento: {resultado})
```

---

## 5. Tecnologias utilizadas

A tabela abaixo detalha as principais ferramentas e dependências adotadas no ecossistema do projeto:

| Módulo | Tecnologia Principal | Versão / Configuração|
| :---: | :--- | ---: |
| **Linguagem** | Python | >=3.10 |
| **Gerenciador de pacotes** | pip | latest |
| **Banco de Dados** | PosgresSQL | 16+ |
| **Motor de SQL** | Metabase | latest |
| **Planilhas** | Excel | 365 |
| **Linguagem** | SQL | pg16+ |
| **Versionamento de código** | Git | latest |
| **Repositório** | Github | latest | 
| **linguagem** | Markdown | latest |

---

## 6. Investigação Científica

- Aborda a fundamentação lógica, o levantamento de hipóteses e a validação metódica de problemas técnicos.
- Aplicada na engenharia para testar arquiteturas , verificar gargalos de performance e documentar premissas de projetos.

---

## 7. Comunicação Empresarial.

- Foco na clareza e objetividade ao registrar artefatos técnicos, facilitando o entendimento entre equipes de desenvolvimento e stakeholders.
- Conecta decisões de engenharia a objetivos de negócio por meio de documentação estruturada.

---

## 8. Git

- Sistema de controle de versão distribuido essencial para gerenciar histórico de alterações de códigos-fonte localmente.
- Permite o rastreamento de mudanças, commits estruturados e segurança no desenvolvimento iterativo.

```bash
# adiciona arquivos ao repo local
git add .

# salva(escreve) os arquivos no repo local 
git commit -m "docs: atualiza documentação dos projetos"

# salva arquivos no repo remoto
git push - u origin feature/add_docs
```

---
## 9. Github

* Plataforma de hospedagem de código que viabiliza o trabalho colaborativo e o armazenamento remoto de repositórios
* Utiliza chaves de acesso seguras e tokens (PAT) para validação de privilégios e publicação de ambientes dedesenvolvimento, homologação e produção.

---
## 10. Markdown

* Linguagem de marcação leve ideal para redigir documentações limpas, padronizadas e legíveis. (`README.md`).
* Permite a integração de títulos, listas de verificação, tabelas dinámicas, blocos de código e formulas científicas.

```markdown
# Título do Módulo
- [x] Tarefa concluída com sucesso

# Exemplo de como declarar uma tabela

|campo 01 | campo 02 | campo 03 |
| --- | --- | --- |
| info_01 | False | 0 |
| info_02 | True | 1 |
```