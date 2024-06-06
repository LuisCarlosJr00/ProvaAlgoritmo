lista =[]
cont = 0


while cont <10:
    
    num = int(input("Digite um numero"))
    
    if num %2 !=0:
        cont +=1
        lista.append(num)
    else:
        print("ERRO! DIGITE NOVAMENTE ")
    
print(lista)