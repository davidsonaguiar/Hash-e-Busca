# Miniprojeto - Aplicações de Hashing e Busca 

## Objetivo:
Aplicar o conhecimento sobre a estrutura de dados "Hashing", bem como sobre as técnicas de busca sequencial e binária em uma aplicação com cadastro de pessoas. 

## Critérios de Avaliação:

1. Executar sem erros 
2. Utilizar implementação do TAD Map (Hashing) 
3. Realizar a especificação solicitada 
4. Indicar qualquer material consultado (codigo, livro, site, etc.) para realização  do trabalho 
 
## Descrição 

Este projeto tem como objetivo avaliar o desempenho de algoritmos e estruturas de dados para inserir dados e realizar buscas de registros no contexto do cadastro nacional de pessoas. O cadastro é composto pelos seguintes campos: CPF (identificador único), nome, telefone e senha. 

**Deve-se desenvolver três estruturas de dados que permitam inserir e pesquisar dados utilizando as seguintes técnicas:**

- Hashing: Utiliza uma tabela hash para armazenar os registros de pessoas, onde o CPF é utilizado como chave de busca. 
- Busca Binária: Os registros são armazenados em uma lista ordenados pelo CPF e utiliza a busca binária para pesquisar os registros. 
- Busca Sequencial: Os registros são armazenados em uma lista não ordenada e a busca é realizada de forma sequencial. 

Para avaliar o desempenho de cada estrutura de dados e dos algoritmos relacionados, realizem testes de inserção e pesquisa com conjuntos de dados de tamanhos variados: 10.000, 100.000 e 1.000.000 de elementos. Em cada teste, registre o tempo médio para inserção e buscar registros. 

## Atividade 

Para executar o projeto sugere-se seguir as seguintes atividades: 

1. **Implementação das Estruturas de Dados:**

- Desenvolva as três estruturas de dados de acordo com as especificações fornecidas. 

- Garanta que as estruturas de dados sejam capazes de inserir registros, buscar registros por CPF e garantir a unicidade do CPF. 

2. **Implementação dos Testes de Desempenho:** 

- Crie funções para gerar CPFs aleatórios e dados de pessoas para inserção nos conjuntos de dados. 

- Implemente testes de inserção para medir o tempo necessário para inserir os registros em cada estrutura de dados. 

- Implemente testes de pesquisa para medir o tempo médio necessário para buscar registros por CPF em cada estrutura de dados. 

3. **Execução dos Testes:**

- Realize os testes com os conjuntos de dados de diferentes tamanhos (10.000, 100.000 e 1.000.000 de elementos). 

- Registre os tempos de inserção e pesquisa para cada estrutura de dados e conjunto de dados. 

4. **Análise de Resultados:**

- Compare os resultados dos testes para cada estrutura de dados e conjunto de dados. 

- Identifique padrões de desempenho e analise como cada estrutura se comporta em diferentes cenários. 

- Interprete os resultados em relação aos objetivos do projeto e aos critérios de avaliação estabelecidos. 

5. **Documentação e Apresentação:** 

- Documente os resultados obtidos, incluindo gráficos e tabelas comparativas. 

- Crie um relatório final descrevendo o projeto, as atividades realizadas, os resultados obtidos e as conclusões alcançadas. 

- Acrescente no relatório uma discussão sobre a seguinte questão: quais considerações devem ser levadas em conta ao decidir por utilizar a busca sequencial, busca binária e hashing nesse projeto. 

## Resposta

Para resolução do projeto criei 3 estruturas

- [ListaOrdenadaSequencial](./estruturas/lista_ordenada_sequencial.py)

- [ListaOrdenadaBinaria](./estruturas/lista_ordenada_binaria.py)

- [TabelaHash](./estruturas/tabela_hash.py)

Nas três estruturas adicionei apenas os métodos necessários para conclusão da atividade e usei como referência o material do classroom.

No início havia criado apenas uma lista sequêncial com os métodos busca_binaria e busca_sequencial, porém resolvi criar duas estruturas em uma a busca e inserção de dados ocorre de forma sequencial e na outro utilizo busca binário para inserir e buscar dados, assim posso testar tanto a busca quanto a inserção dos dados, segue os códigos:

**ListaOrdenadaSequencial**
```
class ListaOrdenadaSequencial:
  
  def __init__(self, capacidade):
    self._capacidade = capacidade
    self._lista = [None] * capacidade
    self._tamanho = 0
    
  
  def tamanho_lista(self):
    return self._tamanho
  
  def esta_cheia(self):
    return self._tamanho == self._capacidade
  
  def esta_vazia(self):
    return self._tamanho == 0
  
  
  def mostrar(self):
    if self.esta_vazia():
      print("A lista está vazia")
      return
    
    for i in range(self._tamanho):
      print(f"CPF: {self._lista[i][0]}, Telefone: {self._lista[i][1]}, Nome: {self._lista[i][2]}")
  
  
  def inserir(self, cpf, telefone, nome, senha):
    
    pessoa = (cpf, telefone, nome, senha)
    
    if self.esta_cheia():
      raise Exception("A lista está cheia")
    
    if self._tamanho == 0: 
      self._lista[0] = pessoa
      self._tamanho += 1
      return
    
    if self._lista[self._tamanho - 1][0] < cpf:
      self._lista[self._tamanho] = pessoa
      self._tamanho += 1
      return
    
    else:
      
      posicao = None
      
      for i in range(self._tamanho):
        if self._lista[i][0] > cpf:
          posicao = i
          break
        
      for i in range(posicao, self.tamanho_lista()):
        self._lista[i + 1] = self._lista[i]
      
      self._lista[posicao] = pessoa
      self._tamanho += 1
      
  def buscar(self, cpf):
    for i in range(self._tamanho):
      if self._lista[i][0] == cpf:
        return self._lista[i]
    return -1
      
```

**ListaOrdenadaBinaria**

```
class ListaOrdenadaBinaria:
  def __init__(self, capacidade):
    self._capacidade = capacidade
    self._lista = [None] * capacidade
    self._tamanho = 0
    
  
  def tamanho_lista(self):
    return self._tamanho
  
  def esta_cheia(self):
    return self._tamanho == self._capacidade
  
  def esta_vazia(self):
    return self._tamanho == 0
  
  
  def mostrar(self):
    if self.esta_vazia():
      print("A lista está vazia")
      return
    
    for i in range(self._tamanho):
      print(f"CPF: {self._lista[i][0]}, Telefone: {self._lista[i][1]}, Nome: {self._lista[i][2]}")
  
  
  def _busca_binaria_inserir(self, cpf):
    inicio = 0
    fim = self._tamanho - 1

    while inicio < fim:
      meio = (inicio + fim) // 2
      
      if self._lista[meio][0] > cpf:
        fim = meio - 1
      else:
        inicio = meio + 1

    return inicio
  
  
  def inserir(self, cpf, telefone, nome, senha):
    
    pessoa = (cpf, telefone, nome, senha)
    
    if self.esta_cheia():
      raise Exception("A lista está cheia")
    
    if self._tamanho == 0: 
      self._lista[0] = pessoa
      self._tamanho += 1
      return
    
    if self._lista[self._tamanho - 1][0] < cpf:
      self._lista[self._tamanho] = pessoa
      self._tamanho += 1
      return
    
    else:
      posicao = None
      
      if self._lista[0][0] > cpf:
        posicao = 0
        
      else:
        posicao = self._busca_binaria_inserir(cpf)
        
      for i in range(posicao, self.tamanho_lista()):
        self._lista[i + 1] = self._lista[i]
      
      self._lista[posicao] = pessoa
      self._tamanho += 1
      
  
  def buscar(self, cpf):
    inicio = 0
    fim = self._tamanho - 1

    while inicio <= fim:
      meio = (inicio + fim) // 2
      
      if self._lista[meio] == None:
        fim = meio - 1
      else:
        if self._lista[meio][0] == cpf:
          return self._lista[meio]
        elif self._lista[meio][0] < cpf:
          inicio = meio + 1
        else:
          fim = meio - 1

    return -1
```

Como informado, utilizei busca binário para inserir os dados, criei o método _busca_binaria_inserir, que retorna o index da posição deve ser inserido o novo registro, evitando percorrer todo o array para isso.

**TabelaHash**

```
class TabelaHash:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.chaves = [None] * capacidade
    self.valores = [None] * capacidade
    self._tamanho = 0
    
  
  def tamanho(self):
    return self._tamanho


  def esta_cheia(self):
    return self._tamanho == self.capacidade
  

  def gerador_hash(self, chave):
    return chave % self.capacidade


  def indice_disponivel(self, indice, chave):
    chave_atual = self.chaves[indice]
    if chave_atual is not None and chave_atual != chave:
      return False
    return True


  def re_hash(self, indice):
    if indice == self.capacidade - 1:
      return 0
    return indice + 1
  

  def inserir(self, cpf, nome, telefone, senha):
    if self.esta_cheia():
      raise Exception("Tabela Hash cheia")

    indice = self.gerador_hash(cpf)

    if self.indice_disponivel(indice, cpf):
      self.chaves[indice] = cpf
      self.valores[indice] = (cpf, nome, telefone, senha)
      self._tamanho += 1
    else:
      indice = self.re_hash(indice)
      while not self.indice_disponivel(indice, cpf):
          indice = self.re_hash(indice)
      self.chaves[indice] = cpf
      self.valores[indice] = cpf
      self._tamanho += 1


  def buscar(self, cpf):
    return self.valores[self.gerador_hash(cpf)]
```

## Testes

**Teste de desempenho para as buscas**

Para o teste criei uma função gerar_dados, que gera os dados solicitados na descrição da atividade cpf, nome, telefone e senha, com intuito de evitar uma demora ao inserir dados na ListaOrdenadaSequencial (já que a intenção do teste é testar a busca), a função gerar CPFs de forma ordenada. 

Essa função possui recebe a quantidade de registros que deve ser gerada e retorna um lista com tuplas `(cpf, nome, telefone, senha)`.

```
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
```

Criei também funcões para inserir todos os registros nas estruturas:

```
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
```

Essa funções apenas são responsáveis por inserir os dados na estrutura e retorna as próprias estruturas já preechidas com os devidos dados para o teste

Depois criei a funçao `teste_desempenho_busca`, que possui uma lista com quantidades de registros para testes `[10000, 100000, 10000000 ]` e pra cada elemento da lista ele inicia uma teste chamando as funcão `gerar_dados`, `teste_busca_sequencial(dados)`, `teste_busca_binaria(dados)`, `teste_busca_hash(dados)`, e para verificar o tempo de busca de cada estrutura segui a dica da descrição da atividade e usei i timeit e gero de forma randómica o cpf para busca.

```
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
    
    print("-" * 50)
```

**Resultado**

- Busca Sequêncial:
  - Teste com 10.000 registros: 0.000443s

  - Teste com 100.000 registros: 0.003893s

  - Teste com 1.000.000 registros: 0.013803s

- Busca Binária:

  - Teste com 10.000 registros: 0.000004s

  - Teste com 100.000 registros: 0.000012s

  - Teste com 1.000.000 registros: 0.000047s

- Busca Hash:

  - Teste com 10.000 registros: 0.0000072s

  - Teste com 100.000 registros: 0.0000032s

  - Teste com 1.000.000 registros: 0.0000030s
