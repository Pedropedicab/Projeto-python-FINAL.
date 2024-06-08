import random

palavras = ("girassol", "casa", "dia", "primavera","sorvete" , "azul","noite")

segredo = random.choices("palavras")

cadeia = "_" * len[segredo]

print(" Bem vindo ao jogo da forca")

tentativas = 0

while True:
    print (cadeia)
    letra = input ("Digite uma letra: ")
    if letra in segredo:
        
        for i in range(len(segredo)):
            if segredo [i] == letra:
                cadeia = cadeia[:i] + letra + cadeia[i+1 :]
                
            else:
                tentativas += 1
                    
                if tentativas == 1:
                    print(" O")
                    
                elif tentativas == 2:
                    print(" O")
                    print("/")
                    
                elif tentativas == 3:
                    print(" O")
                    print("/|")
                    
                elif tentativas == 4:
                    print (" O")
                    print ("/|\\")
                   
                    
                elif tentativas == 5:
                    print (" O")
                    print ("/|\\")
                    print(" /")
                    
                elif tentativas == 6:
                    print(" O")
                    print("/|\\")
                    print("/ \\")
                    
                    print(f"Você perdeu,a palavra secreta era {segredo}")
                    break
                
                if cadeia == segredo:
                    print(f"Parabéns,você ganhou o jogo. A palavra secreta era {segredo}")
                    break
                    
           
                    
   
   
                    
    
    

