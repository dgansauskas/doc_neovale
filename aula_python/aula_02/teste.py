def classificar_risco_credito(idade: int, score: int) -> str:
	"""Retorna a categoria de risco baseada no perfil financeiro."""
	if idade >= 18 and score >= 700:
		return "BAIXO RISCO"
	elif idade >= 18 and score >= 500:
		return "MÉDIO RISCO"
	elif idade >= 18 and score >= 300:
		return "ALTO RISCO"
	elif idade >= 18 and score < 300:
		return "INELEGÍVEL"
	else:
		return "FORA DO ESCOPO"

# Reutilizando a mesma regra para vários clientes:
print(classificar_risco_credito(idade=25, score=820))
print(classificar_risco_credito(idade=18, score=600))
print(classificar_risco_credito(idade=40, score=400))
print(classificar_risco_credito(idade=19, score=299))
print(classificar_risco_credito(idade=17, score=700))