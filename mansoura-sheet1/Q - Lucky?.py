t = int(input())
lista = []
for i in range(t):
    
    l = input()
    for c in l:
        lista.append(int(c))
        
    if sum(lista[:3]) == sum(lista[3:]):
        print("YES")
    else:
        print("NO")
    lista = []
