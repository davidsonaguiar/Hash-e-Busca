class ListaOrdenada:

  def __init__(self):
    self.lista = []

  def tamanho(self):
    return len(self.lista)
  
  def inserir(self, cpf, nome, telefone, senha):
    inicio = 0
    fim = len(self.lista) - 1

    if self.tamanho() == 0:
      self.lista.append((cpf, nome, telefone, senha))
    elif cpf < self.lista[inicio][0]:
      self.lista.insert(inicio, (cpf, nome, telefone, senha))
    else:
      while inicio < fim:
        meio = (inicio + fim) // 2
        if cpf < self.lista[meio][0]:
          fim = meio - 1
        else:
          inicio = meio + 1
      self.lista.insert(inicio + 1, (cpf, nome, telefone, senha))


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