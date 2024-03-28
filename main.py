import random
import timeit

from estruturas.lista_ordenada_binaria import ListaOrdenadaBinaria
from estruturas.lista_ordenada_sequencial import ListaOrdenadaSequencial
from estruturas.tabela_hash import TabelaHash


def gerar_dados(num_registros):
  dados = []
  cpf = 10000000000
  for _ in range(num_registros):
    cpf = cpf + 1
    nome = "Nome" + str(random.randint(1, 1000))
    telefone = "Telefone" + str(random.randint(1, 1000))
    senha = "Senha" + str(random.randint(1, 1000))
    dados.append((cpf, nome, telefone, senha))
    cpf = cpf + 1
  return dados


def teste_busca_sequencial(dados, cpf):
  lista = ListaOrdenadaSequencial(len(dados))
  for pessoa in dados:
    lista.inserir(*pessoa)
  print(lista.tamanho_lista())
  return lista.buscar(cpf)


def teste_busca_binaria(dados, cpf):
  lista = ListaOrdenadaBinaria(len(dados))
  for pessoa in dados:
    lista.inserir(*pessoa)
  return lista.buscar(cpf)


def teste_busca_hash(dados, cpf):
  tabela_hash = TabelaHash(len(dados))
  for pessoa in dados:
    tabela_hash.inserir(*pessoa)
  return tabela_hash.buscar(cpf)


tamanhos = [10000, 100000, 1000000]

for tamanho in tamanhos:
  print(f"Testando desempenho de busca para {tamanho} registros:")
  
  dados = gerar_dados(tamanho)
  cpf_inicial = 10000000000
  cpf_busca = random.randint(10000000000, cpf_inicial + tamanho) 
  
  print(f"CPF de busca: {cpf_busca}")
  
  print()
  
  print("Iniciando teste de busca sequencial...")
  tempo_sequencial = timeit.timeit(lambda: teste_busca_sequencial(dados, cpf_busca), number=1)
  print(f"Tempo de busca sequencial: {tempo_sequencial:.6f} segundos")
  
  print()
  
  print("Iniciando teste de busca binária...")
  tempo_binaria = timeit.timeit(lambda: teste_busca_binaria(dados, cpf_busca), number=1)
  print(f"Tempo de busca binária: {tempo_binaria:.6f} segundos")
  
  print()
  
  print("Iniciando teste de busca em tabela hash...")
  tempo_hash = timeit.timeit(lambda: teste_busca_hash(dados, cpf_busca), number=1)
  print(f"Tempo de busca em tabela hash: {tempo_hash:.6f} segundos")
  
  print("-" * 50)