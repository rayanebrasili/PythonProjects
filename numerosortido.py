from random import randint
 
prog = randint(1, 5)
print("Acerte o número sortiado")

acertou = False
tent = 0
n=0
while not acertou:
    n = int(input("Digite um numero:"))
    tent += 1
    if n == prog:
       acertou = True
       print("acertou o numero na 1°tentativa")
       break
    elif n < prog:
      print("Maior...Tente de novo.")
      
    else:
      print("Menor... Tente de novo")
      print("Acertou com {} tentativas.".format(tent)) 
      break
