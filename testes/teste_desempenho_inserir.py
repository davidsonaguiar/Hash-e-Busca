import random
import timeit
from estruturas.lista_ordenada_binaria import ListaOrdenadaBinaria
from estruturas.lista_ordenada_sequencial import ListaOrdenadaSequencial
from estruturas.tabela_hash import TabelaHash


def gerar_dados(num_registros):
  cpf_set = set()
  dados = []
  
  while len(cpf_set) < num_registros:
    cpf = random.randint(10000000000, 99999999999)
    cpf_set.add(cpf)
  
  for cpf in cpf_set:
    nome = "Pessoa Teste"
    telefone = "99999999999"
    senha ="senha"
    dados.append((cpf, nome, telefone, senha))
  
  return dados


def teste_inserir_sequencial(dados):
  lista = ListaOrdenadaSequencial(len(dados))
  for pessoa in dados:
    lista.inserir(*pessoa)
  print(lista.tamanho_lista())
  

def teste_inserir_binaria(dados):
  lista = ListaOrdenadaBinaria(len(dados))
  for pessoa in dados:
    lista.inserir(*pessoa)
  print(lista.tamanho_lista())
    

def teste_inserir_hash(dados):
  tabela_hash = TabelaHash(len(dados))
  for pessoa in dados:
    tabela_hash.inserir(*pessoa)
  print(tabela_hash.tamanho())
    
    
def teste_desempenho_inserir():
  tamanhos = [10000, 100000, 1000000]
  
  for tamanho in tamanhos:
    print(f"Testando desempenho de inserção para {tamanho} registros:")
    
    dados = gerar_dados(tamanho)
        
    print("Iniciando teste de inserção binária...")
    tempo_binaria = timeit.timeit(lambda: teste_inserir_binaria(dados), number=1)
    print(f"Tempo de inserção binária: {tempo_binaria:.6f} segundos")
    
    print("Iniciando teste de inserção hash...")
    tempo_hash = timeit.timeit(lambda: teste_inserir_hash(dados), number=1)
    print(f"Tempo de inserção hash: {tempo_hash:.6f} segundos")
    
    print("Iniciando teste de inserção sequencial...")
    tempo_sequencial = timeit.timeit(lambda: teste_inserir_sequencial(dados), number=1)
    print(f"Tempo de inserção sequencial: {tempo_sequencial:.6f} segundos")
    
    print()
    print("=" * 50)