import random
import timeit

from estruturas.lista_ordenada_binaria import ListaOrdenadaBinaria
from estruturas.lista_ordenada_sequencial import ListaOrdenadaSequencial
from estruturas.tabela_hash import TabelaHash


def gerar_dados(num_registros):
  dados = []
  cpf = 10000000000
  for i in range(num_registros):
    cpf = cpf
    nome = "Nome" + str(i)
    telefone = "Telefone" + str(i) 
    senha = "Senha" + str(i)
    dados.append((cpf, nome, telefone, senha))
    cpf = cpf + 1
  return dados


def teste_busca_sequencial(dados):
  lista = ListaOrdenadaSequencial(len(dados))
  for pessoa in dados:
    lista.inserir(*pessoa)
  return lista


def teste_busca_binaria(dados):
  lista = ListaOrdenadaBinaria(len(dados))
  for pessoa in dados:
    lista.inserir(*pessoa)
  return lista


def teste_busca_hash(dados):
  tabela_hash = TabelaHash(len(dados))
  for pessoa in dados:
    tabela_hash.inserir(*pessoa)
  return tabela_hash


def teste_desempenho_busca():
  tamanhos = [10000, 100000, 1000000]

  for tamanho in tamanhos:
    print(f"Testando desempenho de busca para {tamanho} registros:")
    
    dados = gerar_dados(tamanho)
    cpf_inicial = 10000000000
    cpf_busca = random.randint(10000000000, cpf_inicial + tamanho) 
    
    print(f"CPF de busca: {cpf_busca}")
    print()

    print("Iniciando teste de busca sequencial...") 
    teste_sequencial = teste_busca_sequencial(dados)
    tempo_sequencial = timeit.timeit(lambda: teste_sequencial.buscar(cpf_busca), number=1)
    print(teste_sequencial.buscar(cpf_busca))
    print(f"Tempo de busca sequencial: {tempo_sequencial:.6f} segundos")
    
    print()
    
    print("Iniciando teste de busca binária...")
    teste_binaria = teste_busca_binaria(dados)
    tempo_binaria = timeit.timeit(lambda: teste_binaria.buscar(cpf_busca), number=1)
    print(teste_binaria.buscar(cpf_busca))
    print(f"Tempo de busca binária: {tempo_binaria:.6f} segundos")
    
    print()
    
    print("Iniciando teste de busca em tabela hash...")
    teste_hash = teste_busca_hash(dados)
    tempo_hash = timeit.timeit(lambda: teste_hash.buscar(cpf_busca), number=1)
    print(teste_hash.buscar(cpf_busca))
    print(f"Tempo de busca em tabela hash: {tempo_hash:.7f} segundos")
    
    print("=" * 50)
    