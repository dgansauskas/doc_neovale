# VARIAVEIS
# nome = 'Danilo C.'
# idade = 46

# print(f'Meu nome é {nome}' )
# print(f'Minha idade é {idade}')

# # ----------------------------------------------------------
# # LISTAS
# cidades = ['Campo Grande','Ponta Porã', 'São Miguel']

# # acrescentar uma cidade:
# cidades.append('São Paulo')
# # cidades.remove('São Miguel')
# cidades.pop(2)

# print(cidades)

# for indice,cidade in enumerate(cidades):
#     if not indice in (1,3):
#         print(f'Eu moro em {cidade} e seu índice é {indice}')

# ----------------------------------------------------------
# DICIONARIOS

cliente = {
	"id": 101,
	"nome": "Ana Silva",
	"idade": 29,
	"email": "ana.silva@email.com",
	"ativo": True
}

print(type(cliente))
# cliente["nome"]='Danilo'
cliente["ativo"]=False
print(cliente["ativo"])