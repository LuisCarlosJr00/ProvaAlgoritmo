produto= {}
   
lista = []

def descricao():
    produto["item"] = input("Item: ")
    produto["valor"] = float(input("Valor: "))
    lista.append(produto.copy())

for i in range (0,5):
    descricao()
    
print(lista)
    
