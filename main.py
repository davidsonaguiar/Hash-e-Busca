from lista_ordenada import ListaOrdenada

lista = ListaOrdenada(3)

lista.inserir(1, 'João', '1234-5678', '1234')
lista.inserir(2, 'Maria', '1234-5678', '1234')
lista.inserir(3, 'José', '1234-5678', '1234')

print(lista.buscar_binaria(1))
