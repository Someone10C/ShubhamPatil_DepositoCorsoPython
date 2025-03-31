numeri= []
print ("Per favore inserisci una lista di numeri: ")
numeri = input().split()
pos = 0
for pos, var in enumerate(numeri):
    numeri[pos] = int(var) **2

print(numeri)
