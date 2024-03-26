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
    indice = self.gerador_hash(cpf)
    return self.valores[indice]
  

  def __str__(self):
    pessoas = []
    for i in range(self.capacidade):
      if self.chaves[i] is not None:
        pessoa = self.valores[i]
        pessoas.append(f"CPF: {pessoa[0]}, Nome: {pessoa[1]}, Telefone: {pessoa[2]}, Senha: {pessoa[3]}")
    return "\n".join(pessoas)
  