# multipla escolha 
print("escolha a fruta que voce deseja comprar")
print("maça = 1")
print("laranja = 2")
print("banana = 3")
#agr deixe o usuario realizar escolha
produto = int(input("qual comprar? "))
if(produto == 1):
    print("voce escolheu maças")
    print("o preço da maça e de 2.3 reais")
    quantidade = int(input("qual a quantidade?"))
    total = (quantidade*2.3)
    print(f"voce comprou {quantidade} de maças, o total sera de: {total}")
elif(produto == 2):
        print("voce escolheu laranjas")
        print("o preço da laranja e de 3 reais")
        quantidade = int(input("qual a quantidade? "))
        total = (quantidade*3)
        print(f"voce comprou um total de {quantidade} de laranjas, o preço total sera de: {total}")

elif(produto == 3):

    print("voce escolheu bananas")
    print("o preço da banana e de 3.45")
    quantidade = int(input("qual a quantidade? "))
    total = (quantidade* 3.45 )
    print(f"voce comprou {quantidade} de bananas, o total sera de: {total} reais")
else:
     print("produto inexistente")
