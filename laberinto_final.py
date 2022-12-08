
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

def laberinto_final(laberinto):
    #inicializar fila y columna
    columna = 0
    fila = 0
    #inicializar lista para guardar los movimientos
    solucion = ['Inicio']
    #bucle para que mientras que no se salga del laberinto ni llegue a la salida'S' 
    #seguira moviéndose hasta encontrar la salida ('S')
    while ( fila <= 5 and columna <= 5) and laberinto[fila][columna] != 'S': #5 es la longitud del laberinto tanto para sus filas y sus columanas ya que es un cuadrado
