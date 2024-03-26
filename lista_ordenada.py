class ListaOrdenada:

  def __init__(self, capacidade):
    self.lista = [None] * capacidade
    self._tamanho = 0
    
  
  def esta_cheia(self):
    return self.tamanho() == len(self.lista)
    

  def tamanho(self):
    return self._tamanho
  
  
  def buscar_binaria_para_inserir(self, cpf):
    inicio = 0
    fim = len(self.lista) - 1

    while inicio < fim:
      meio = (inicio + fim) // 2
      if (self.lista[meio] == None):
        fim = meio - 1
      elif cpf < self.lista[meio][0]:
        fim = meio - 1
      else:
        inicio = meio + 1

    return inicio
  
  
  def inserir(self, cpf, nome, telefone, senha):
     
    if self.esta_cheia():
      raise Exception('A lista está cheia')
    
    if self.tamanho() == 0:
      self.lista[self.tamanho()] = (cpf, nome, telefone, senha)
      self._tamanho += 1    
    else:
      posicao = None
      if cpf < self.lista[0][0]:
        posicao = 0
      else:
        posicao = self.buscar_binaria_para_inserir(cpf)
        
      for i in range(posicao, self.tamanho()):     
        self.lista[i+1] = self.lista[i]
      
      self.lista[posicao] = (cpf, nome, telefone, senha)
      self._tamanho += 1
    

  def buscar_sequencial(self, cpf):
    if cpf < self.lista[0][0] or cpf > self.lista[-1][0]:
      return None
    else:
      for i in range(len(self.lista)):
        if self.lista[i][0] == cpf:
          return self.lista[i]
        if cpf < self.lista[i][0]:
          return None
        

  def buscar_binaria(self, cpf):

    inicio = 0
    fim = len(self.lista) - 1

    while inicio <= fim:
      meio = (inicio + fim) // 2
      if self.lista[meio][0] == cpf:
        return self.lista[meio]
      elif cpf < self.lista[meio][0]:
        fim = meio - 1
      else:
        inicio = meio + 1
    return None
  

  def print_lista(self):
    for pessoa in self.lista:
      print(pessoa)