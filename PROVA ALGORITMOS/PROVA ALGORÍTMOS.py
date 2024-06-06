
lista_numeros= [1,2,3,4,5,6,7,8,9,10]

user = int(input("Digite um número: "))

for i in range (0,len(lista_numeros)):
    if user == lista_numeros[i]:
        print(f" >>>O número digitado está presente na lista de números cadastrados, na posição {lista_numeros[i]}<<< ")
        break
else:
    print(" >>>O número NÃO faz parte da lista <<< ")
        