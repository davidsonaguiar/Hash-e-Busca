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
      