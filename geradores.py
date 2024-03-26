import random

from lista_ordenada import ListaOrdenada
from tabela_hash import TabelaHash

def gerar_dados(num_registros):
  dados = []
  for _ in range(num_registros):
    cpf = random.randint(1, num_registros * 10)
    nome = "Nome" + str(random.randint(1, 1000))
    telefone = "Telefone" + str(random.randint(1, 1000))
    senha = "Senha" + str(random.randint(1, 1000))
    dados.append((cpf, nome, telefone, senha))
  return dados


def teste_busca_sequencial(dados, cpf):
  lista = ListaOrdenada()
  for pessoa in dados:
    lista.inserir(*pessoa)
  return lista.buscar_sequencial(cpf)


def teste_busca_binaria(dados, cpf):
  lista = ListaOrdenada()
  for pessoa in dados:
    lista.inserir(*pessoa)
  return lista.buscar_binaria(cpf)


def teste_busca_hash(dados, cpf):
  tabela_hash = TabelaHash(capacidade=len(dados) * 2)
  for pessoa in dados:
    tabela_hash.inserir(*pessoa)
  return tabela_hash.buscar(cpf)