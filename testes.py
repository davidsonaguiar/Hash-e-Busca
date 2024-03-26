import random
import timeit

from geradores import gerar_dados, teste_busca_binaria, teste_busca_hash, teste_busca_sequencial

tamanhos = [10000, 100000, 1000000]

for tamanho in tamanhos:
  print(f"Testando desempenho para {tamanho} registros:")
  dados = gerar_dados(tamanho)
  
  cpf_busca = random.randint(1, tamanho * 10) 
  
  tempo_sequencial = timeit.timeit(lambda: teste_busca_sequencial(dados, cpf_busca), number=1)
  print(f"Tempo de busca sequencial: {tempo_sequencial:.6f} segundos")
  
  tempo_binaria = timeit.timeit(lambda: teste_busca_binaria(dados, cpf_busca), number=1)
  print(f"Tempo de busca binária: {tempo_binaria:.6f} segundos")
  
  tempo_hash = timeit.timeit(lambda: teste_busca_hash(dados, cpf_busca), number=1)
  print(f"Tempo de busca em tabela hash: {tempo_hash:.6f} segundos")
  
  print("-" * 50)