
def snail(snail_map):
    
    snail1 = []
    while True:
        n = len(snail_map)
        
        snail1.extend(snail_map[0])
        if n == 0:
            return snail1
        if n == 1:
            return snail1    
        elif n == 2:
            snail1.append(snail_map[1][1])
            snail1.append(snail_map[1][0])
            return snail1

        columna = [fila[n-1] for fila in snail_map]
        columna1 = [fila[0] for fila in snail_map]
        columna.pop(0)
        columna1.pop(0)
        fila = snail_map[n-1]
        fila.pop(0)
        fila.pop(n-2)
        snail1.extend(columna)
        snail1.extend(reversed(fila))
        snail1.extend(reversed(columna1))
        snail_map.pop(0)
        snail_map.pop(n-2)

        for i in range(n-2) :
            snail_map[i].pop(n-1)
            snail_map[i].pop(0)
       
    
print(snail([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
'''
[1,2, 3, 4]
[5,6, 7, 8]
[9,10,11,12]
[13,14,15,16]

'''