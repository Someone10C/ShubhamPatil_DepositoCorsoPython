numeri= []
print ("Per favore inserisci una lista di numeri: ")
numeri = input().split()
max = numeri[0]
# for loop per controllare se la lista è vuota
if numeri == []:
    print("La lista è vuota")
    
else:
    print("La lista non è vuota")
    # for loop per cercare max
    for val in numeri :
        if max < val:  
            max = val

    print("Il numero più grande è:",max)

    # while loop per numeri di elimenti in una lista
    val = 0
    while val in range(int(max)):
        val = val + 1  
    print("La lista contiene:",val)  




 