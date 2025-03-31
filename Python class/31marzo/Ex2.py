print("Per favore inserisci un numero intero: ")
numero_2 = input()
var = 0
list= []
while var in range(int(numero_2)):
    list.append(var)
    var = var + 1
list.append(var)
list.reverse()
print(list)