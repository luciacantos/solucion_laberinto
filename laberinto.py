def laberinto(dimension, muros):
    #creamos lista
    laberinto = []

    for i in range(dimension):
        fila = []
        for j in range(dimension):
            fila.append('')
        laberinto.append(fila)

    for muro in muros:
        laberinto[muro[0]][muro[1]] = 'X'

    laberinto[dimension-1][dimension-1] = 'S'

    return laberinto

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
x = laberinto(5,muro)
print(x)
